# команды бота
from aiogram import types
from aiogram.dispatcher.filters import Command

from main import dp, usr
from src.bot_comands.admin_cmd import adm_start
from src.Role.users.user import User


@dp.message_handler(Command("start"))
async def cmd_start(msg: types.Message):
    await adm_start(msg)
    await User().chk_usr(msg)
    # await msg.answer(usr.q_txt[0], reply_markup=await usr.auth_kb())


@dp.message_handler(Command("profile"))
async def profile(msg: types.Message):
    await usr.show_profile(msg)
