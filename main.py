import asyncio
from aiogram import Dispatcher, executor, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from configs.config import TOKEN
from groups.user.user import User
from mydb.db import MyDB

mydb = MyDB()
usr = User()
bot = Bot(token=TOKEN)

event_loop = asyncio.get_event_loop()
dp = Dispatcher(bot, loop=event_loop, storage=MemoryStorage())

if __name__ == "__main__":
    from handlers.cmd_handlers.cmd_handler import dp
    from handlers.menu_handler.menu_handler import dp
    from groups.user.user_handler import dp
    executor.start_polling(dp, skip_updates=True)
