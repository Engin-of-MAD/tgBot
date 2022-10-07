# команды бота
from aiogram import types
from aiogram.dispatcher.filters import Command

import mydb.db
from src.bot_comands import adm_start
from main import dp, usr, mydb


@dp.message_handler(Command("start"))
async def cmd_start(msg: types.Message):
    await adm_start(msg)
    mydb.check_user_in_stud(msg)
    await msg.answer(usr.q_txt[0], reply_markup=await usr.auth_kb())


@dp.message_handler(Command("profile"))
async def profile(msg: types.Message):
    await usr.show_profile(msg)
