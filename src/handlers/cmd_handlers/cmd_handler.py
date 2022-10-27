from aiogram import types
from aiogram.dispatcher.filters import Command

from main import dp
from src.bot_comands.admin_cmd import adm_start
from src.Role.users.user import User

############################################################
# команды бота


@dp.message_handler(Command("start"))
async def cmd_start(msg: types.Message):
    await adm_start(msg)
    User().set_userdata(uid=msg.from_user.id)
    await User().chk_usr(msg)


@dp.message_handler(Command("profile"))
async def profile(msg: types.Message):
    usr = User(msg.from_user.id)
    await usr.show_profile(msg)


@dp.message_handler(Command("lessons"))
async def lessons(msg: types.Message):
    await User().show_lessons(msg)
