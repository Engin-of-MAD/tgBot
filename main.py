import asyncio
from aiogram import Dispatcher, executor, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from src.configs.config import TOKEN
from src.groups.user.user import User
from src.db.db import MyDB


usr = User()
mydb = MyDB()
bot = Bot(token=TOKEN)

event_loop = asyncio.get_event_loop()
dp = Dispatcher(bot, loop=event_loop, storage=MemoryStorage())

if __name__ == "__main__":
    from src.handlers.cmd_handlers import dp
    from src.handlers.menu_handler import dp
    from src.groups.user import dp
    executor.start_polling(dp, skip_updates=True)
