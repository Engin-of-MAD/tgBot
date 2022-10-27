from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inl_btn1 = InlineKeyboardButton(text="11:00-12:00", callback_data="btn1")
inl_btn2 = InlineKeyboardButton(text="12:00-13:00", callback_data="btn2")
inl_btn3 = InlineKeyboardButton(text="13:00-14:00", callback_data="btn3")
inl_btn4 = InlineKeyboardButton(text="14:00-15:00", callback_data="btn4")
inl_btn5 = InlineKeyboardButton(text="15:00-16:00", callback_data="btn5")
inl_btn6 = InlineKeyboardButton(text="16:00-17:00", callback_data="btn6")
inl_btn7 = InlineKeyboardButton(text="17:00-18:00", callback_data="btn7")
inl_btn8 = InlineKeyboardButton(text="18:00-19:00", callback_data="btn8")
inl_btn9 = InlineKeyboardButton(text="19:00-20:00", callback_data="btn8")
inl_btn10 = InlineKeyboardButton(text="20:00-21:00", callback_data="btn10")


async def aud_menu_kb() -> InlineKeyboardMarkup:
    aud_kb = InlineKeyboardMarkup()
    aud_kb.add(inl_btn1)
    aud_kb.add(inl_btn2)
    aud_kb.add(inl_btn3)
    aud_kb.add(inl_btn4)
    aud_kb.add(inl_btn5)
    aud_kb.add(inl_btn6)
    aud_kb.add(inl_btn7)
    aud_kb.add(inl_btn8)
    aud_kb.add(inl_btn9)
    aud_kb.add(inl_btn10)
    return aud_kb
