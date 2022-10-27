from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inl_btn1 = InlineKeyboardButton("11:00 - 13:00", callback_data='button1')
inl_btn2 = InlineKeyboardButton("13:00 - 15:00", callback_data='button2')
inl_btn3 = InlineKeyboardButton("15:00 - 17:00", callback_data='button3')
inl_btn4 = InlineKeyboardButton("17:00 - 19:00", callback_data='button4')
inl_btn5 = InlineKeyboardButton("19:00 - 21:00", callback_data='button5')


async def sch_menu():
    sch_kb = InlineKeyboardMarkup()
    sch_kb.add(inl_btn1)
    sch_kb.add(inl_btn2)
    sch_kb.add(inl_btn3)
    sch_kb.add(inl_btn4)
    sch_kb.add(inl_btn5)
    return sch_kb
