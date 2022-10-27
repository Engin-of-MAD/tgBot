from main import dp
from src.callback_data.days_cb import days_data

from aiogram import types


@dp.callback_query_handler(days_data.filter(day="Mon"))
async def mon(call: types.CallbackQuery):
    pass
