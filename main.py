import asyncio
from aiogram import Dispatcher, executor, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from src.configs.config import TOKEN


bot = Bot(token=TOKEN)

event_loop = asyncio.get_event_loop()
dp = Dispatcher(bot, loop=event_loop, storage=MemoryStorage())

if __name__ == "__main__":
    from src.handlers.cmd_handlers.cmd_handler import dp
    from src.handlers.menu_handler.menu_handler import dp
    from src.handlers.users_handlers.user_handler import dp
    from src.handlers.inl_handler.grpl_handler import dp
    from src.handlers.inl_handler.order_handler import dp
    executor.start_polling(dp, skip_updates=True)
