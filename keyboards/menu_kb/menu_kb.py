from aiogram import types

btn_schL = types.KeyboardButton("Расписание занятий")
btn_repA = types.KeyboardButton("Репетиционные Аудитории")
btn_a = types.KeyboardButton("Аудитория А")
btn_b = types.KeyboardButton("Аудитория B")
btn_info = types.KeyboardButton("Info")
btn_back = types.KeyboardButton("Назад")
btn_grpL = types.KeyboardButton("Групповые Занятия")
btn_perL = types.KeyboardButton("Индивидуальные Занятия")
btn_bToMain = types.KeyboardButton("Вернуться в главное меню")


async def main_menu() -> types.ReplyKeyboardMarkup:
    bs_kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    bs_kb.add(btn_schL)
    bs_kb.add(btn_repA)
    bs_kb.add(btn_info)
    return bs_kb



async def menu_sch_aud() -> types.ReplyKeyboardMarkup:
    aud_kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    aud_kb.add(btn_a)
    aud_kb.add(btn_b)
    aud_kb.add(btn_info)
    aud_kb.add(btn_back)
    return aud_kb


async def menu_sch_les() -> types.ReplyKeyboardMarkup:
    les_kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    les_kb.add(btn_grpL)
    les_kb.add(btn_perL)
    les_kb.add(btn_info)
    les_kb.add(btn_bToMain)
    return les_kb


