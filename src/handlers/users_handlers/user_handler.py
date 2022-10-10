from main import dp, bot, usr, mydb
from src.keyboards.inline_kb.call_data import auth_data
from src.fsm.user_fsm import Usr
from src.fsm.menu_fsm import Menu
from src.keyboards.menu_kb.menu_kb import MyKb
from src.Role.users.user import User

from aiogram.dispatcher import FSMContext
from aiogram import types

kb = MyKb()

#####################################################################
# Диалоговая клавиатура


@dp.callback_query_handler(auth_data.filter(yn="yes"))
async def not_auth_user(call: types.CallbackQuery):
    usr.auth_user = True
    await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text=usr.q_txt[1])
    await Usr.f_name.set()


@dp.callback_query_handler(auth_data.filter(yn="no"))
async def yet_auth_user(call: types.CallbackQuery):
    usr.auth_user = False
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await Menu.menu_switch.set()

#####################################################################
# Регистрация и инициализация пользователя
# Имя


@dp.message_handler(state=Usr.f_name)
async def first_name_handler(msg: types.Message, state: FSMContext):
    await state.update_data(f_name=msg.text)
    await msg.answer(text=User.q_txt[2])
    await Usr.l_name.set()

#####################################################################
# Фамилия


@dp.message_handler(state=Usr.l_name)
async def last_name_handler(msg: types.Message, state: FSMContext):
    await state.update_data(l_name=msg.text)
    await msg.answer(text=usr.q_txt[3], reply_markup=await kb.phone_kb())
    await Usr.phone.set()

#####################################################################
# Номер телефона


@dp.message_handler(state=Usr.phone, content_types=types.ContentTypes.CONTACT)
async def phone_handler(msg: types.Message, state: FSMContext):
    data = await state.get_data()

    usr.first_name = data["f_name"]
    usr.last_name = data["l_name"]
    usr.set_tg_id(msg)
    usr.set_tg_name(msg)
    usr.set_phone(msg.contact.phone_number)

    await state.update_data(phone=msg.contact.phone_number)
    await state.update_data(tg_id=usr.get_tg_id())
    await state.update_data(tg_nickname=usr.get_tg_id())
    await usr.show_profile(msg)
    await state.finish()
    await usr.gen_data()
    mydata = await usr.gen_data()
    await mydb.insert_to_stud(**mydata)
    await msg.answer(text=User().q_txt[4])

    await msg.answer(text="Пожалуйста выберете пункт меню", reply_markup=await MyKb().main_menu())


