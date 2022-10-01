# команды бота
from aiogram import types
from aiogram.dispatcher.filters import Command

from bot_comands.admin_cmd import adm_start
from main import dp, usr


@dp.message_handler(Command("start"))
async def cmd_start(msg: types.Message):
    await adm_start(msg)
    await msg.answer(usr.q_txt[0], reply_markup=await usr.auth_kb())


@dp.message_handler(Command("profile"))
async def profile(msg: types.Message):
    await usr.show_profile(msg)
