from main import dp, bot, usr


from inline.call_data import auth_data


from fsm.user_fsm import FIO
from fsm.menu_fsm import MenuCtrl

from aiogram.dispatcher import FSMContext
from aiogram import types


@dp.callback_query_handler(auth_data.filter(yn="yes"))
async def not_auth_user(call: types.CallbackQuery):
    usr.greeting_msg = True
    await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text=usr.q_txt[1])
    await FIO.fio.set()
    """await bot.edit_message_text(chat_id=call.from_user.id,
                                message_id=call.message.message_id,
                                text=usr.q_txt[1])
    await bot.edit_message_reply_markup(chat_id=call.from_user.id,
                                        message_id=call.message.message_id,
                                        reply_markup=await usr.q2())
"""


@dp.callback_query_handler(auth_data.filter(yn="no"))
async def yet_auth_user(call: types.CallbackQuery):
    usr.greeting_msg = False
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await MenuCtrl.menu_switch.set()


@dp.message_handler(state=FIO.fio)
async def first_name_handler(msg: types.Message, state: FSMContext):
    await state.update_data(fi=msg.text)
    await FIO.out_fio.set()


@dp.message_handler(state=FIO.out_fio)
async def last_name_handler(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    await msg.answer(f"Ваше Имя и Фамилия: {data['fi']}")
    await MenuCtrl.menu_switch.set()


