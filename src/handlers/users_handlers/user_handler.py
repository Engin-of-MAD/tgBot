from main import dp, bot
from src.callback_data.auth_cb import auth_data
from src.fsm.user_fsm import Usr
from src.fsm.menu_fsm import Menu
from src.keyboards.menu_kb.menu_kb import MyKb
from src.Role.users.user import User
from src.db.db import MyDB

from aiogram.dispatcher import FSMContext
from aiogram import types

kb = MyKb()
mydb = MyDB()
#####################################################################
# Диалоговая клавиатура


@dp.callback_query_handler(auth_data.filter(yn="yes"))
async def not_auth_user(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text=User().q_txt[1])
    await Usr.f_name.set()


@dp.callback_query_handler(auth_data.filter(yn="no"))
async def yet_auth_user(call: types.CallbackQuery):
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
    await msg.answer(text=User().q_txt[3], reply_markup=await kb.phone_kb())
    await Usr.phone.set()

#####################################################################
# Номер телефона


@dp.message_handler(state=Usr.phone, content_types=types.ContentTypes.CONTACT)
async def phone_handler(msg: types.Message, state: FSMContext):
    data = await state.get_data()

    User().set_tg_id(msg)
    User().set_tg_name(msg)
    User().set_phone_num(msg)
    User.set_first_name(data)
    User.set_last_name(data)
    await state.finish()

    await User().show_profile(msg)

    mydata = await User().gen_data()
    await mydb.insert_to_stud(**mydata)
    await msg.answer(text=User().q_txt[4])
    await msg.answer(text="Пожалуйста выберете пункт меню", reply_markup=await MyKb().main_menu())


