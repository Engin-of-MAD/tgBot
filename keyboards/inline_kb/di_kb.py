from aiogram import types
from aiogram.utils.callback_data import CallbackData


async def yn_kb(cb: CallbackData):
    inl_btn_y = types.InlineKeyboardButton(text="Да", callback_data=cb.new(yn="yes"))
    inl_btn_n = types.InlineKeyboardButton(text="Нет", callback_data=cb.new(yn="no"))
    yn = types.InlineKeyboardMarkup(row_width=1)
    yn.add(inl_btn_y)
    yn.add(inl_btn_n)
    return yn
