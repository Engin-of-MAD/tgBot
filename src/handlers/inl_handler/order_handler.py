from main import dp, bot

from src.callback_data.time_cb import time_data as time_d
from src.callback_data.days_cb import days_data
from src.callback_data.aud_cb import aud_data

from src.Role.users.user import User

from src.keyboards.menu_kb.menu_kb import MyKb
from src.keyboards.inline_kb.inl_kb import InlMenu

from src.db.lessons_db import LessonDb

from aiogram import types
from datetime import date, time
from src.dtchk.date_chk import DateCheck

lesson_db = LessonDb()
dt = DateCheck(date.today().day, date.today().month, date.today().year)
tmp = []
#####################################################################################
# Выбор аудиторий


@dp.callback_query_handler(aud_data.filter(aud="Aud_A"))
async def aud_a(call: types.CallbackQuery):
    lesson_db.data.update(st_tg_id=call.from_user.id)
    print(User(call.from_user.id).tg_id)
    lesson_db.data.update(aud="Аудитория A")
    inl_kb = await InlMenu().chs_day(days_data)
    await bot.edit_message_text(chat_id=call.from_user.id,
                                message_id=call.message.message_id,
                                text=MyKb.m_txt[6], reply_markup=inl_kb)


@dp.callback_query_handler(aud_data.filter(aud="Aud_B"))
async def aud_a(call: types.CallbackQuery):
    lesson_db.data.update(st_tg_id=call.from_user.id)
    lesson_db.data.update(aud="Аудитория B")
    inl_kb = await InlMenu().chs_day(days_data)
    await bot.edit_message_text(chat_id=call.from_user.id,
                                message_id=call.message.message_id,
                                text=MyKb.m_txt[6], reply_markup=inl_kb)

#####################################################################################
#  Выбор дня недели занятия


@dp.callback_query_handler(days_data.filter(day="Mond"))
async def day_mon_handler(call: types.CallbackQuery):
    lesson_db.data.update(day="Понедельник")
    inl_kb = await InlMenu().grpl_time()
    await bot.edit_message_text(chat_id=call.from_user.id,
                                message_id=call.message.message_id,
                                text=InlMenu().inl_txt[0], reply_markup=inl_kb)
    dt.set_date(1)


@dp.callback_query_handler(days_data.filter(day="Tue"))
async def day_tue_handler(call: types.CallbackQuery):
    lesson_db.data.update(day="Вторник")
    inl_kb = await InlMenu().grpl_time()
    await bot.edit_message_text(chat_id=call.from_user.id,
                                message_id=call.message.message_id,
                                text=InlMenu().inl_txt[0], reply_markup=inl_kb)
    dt.set_date(2)


@dp.callback_query_handler(days_data.filter(day="Wed"))
async def day_wed_handler(call: types.CallbackQuery):
    lesson_db.data.update(day="Среда")
    inl_kb = await InlMenu().grpl_time()
    await bot.edit_message_text(chat_id=call.from_user.id,
                                message_id=call.message.message_id,
                                text=InlMenu().inl_txt[0], reply_markup=inl_kb)
    dt.set_date(3)


@dp.callback_query_handler(days_data.filter(day="Thu"))
async def day_thu_handler(call: types.CallbackQuery):
    lesson_db.data.update(day="Четверг")
    inl_kb = await InlMenu().grpl_time()
    await bot.edit_message_text(chat_id=call.from_user.id,
                                message_id=call.message.message_id,
                                text=InlMenu().inl_txt[0], reply_markup=inl_kb)
    dt.set_date(4)


@dp.callback_query_handler(days_data.filter(day="Fri"))
async def day_fri_handler(call: types.CallbackQuery):
    lesson_db.data.update(day="Пятница")
    inl_kb = await InlMenu().grpl_time()
    await bot.edit_message_text(chat_id=call.from_user.id,
                                message_id=call.message.message_id,
                                text=InlMenu().inl_txt[0], reply_markup=inl_kb)
    dt.set_date(5)


@dp.callback_query_handler(days_data.filter(day="Sat"))
async def day_sat_handler(call: types.CallbackQuery):
    lesson_db.data.update(day="Суббота")
    inl_kb = await InlMenu().grpl_time()
    await bot.edit_message_text(chat_id=call.from_user.id,
                                message_id=call.message.message_id,
                                text=InlMenu().inl_txt[0], reply_markup=inl_kb)
    dt.set_date(6)


@dp.callback_query_handler(days_data.filter(day="Sun"))
async def day_sun_handler(call: types.CallbackQuery):
    lesson_db.data.update(day="Воскресенье")
    inl_kb = await InlMenu().grpl_time()
    await bot.edit_message_text(chat_id=call.from_user.id,
                                message_id=call.message.message_id,
                                text=InlMenu().inl_txt[0], reply_markup=inl_kb)
    dt.set_date(7)

#####################################################################################
# время групповых занятий


@dp.callback_query_handler(time_d.filter(time="btn0g"))
async def time_btn0g_handler(call: types.CallbackQuery):
    lesson_db.data.update(date=f"{dt.m_dt} {time(hour=11, minute=0, second=0)}")
    await User().chk_lessons(uid=call.from_user.id, call=call)


@dp.callback_query_handler(time_d.filter(time="btn1g"))
async def time_btn1g_handler(call: types.CallbackQuery):
    lesson_db.data.update(date=f"{dt.m_dt} {time(hour=13, minute=0, second=0)}")
    await User().chk_lessons(uid=call.from_user.id, call=call)


@dp.callback_query_handler(time_d.filter(time="btn2g"))
async def time_btn2g_handler(call: types.CallbackQuery):
    lesson_db.data.update(date=f"{dt.m_dt} {time(hour=15, minute=0, second=0)}")
    await User().chk_lessons(uid=call.from_user.id, call=call)


@dp.callback_query_handler(time_d.filter(time="btn3g"))
async def time_btn3g_handler(call: types.CallbackQuery):
    lesson_db.data.update(date=f"{dt.m_dt} {time(hour=17, minute=0, second=0)}")
    await User().chk_lessons(uid=call.from_user.id, call=call)


@dp.callback_query_handler(time_d.filter(time="btn4g"))
async def time_bt4g_handler(call: types.CallbackQuery):
    lesson_db.data.update(date=f"{dt.m_dt} {time(hour=19, minute=0, second=0)}")
    await User().chk_lessons(uid=call.from_user.id, call=call)


@dp.callback_query_handler(time_d.filter(time="btn5g"))
async def time_btn5g_handler(call: types.CallbackQuery):
    lesson_db.data.update(date=f"{dt.m_dt} {time(hour=21, minute=0, second=0)}")
    await User().chk_lessons(uid=call.from_user.id, call=call)

#####################################################################################
# Время персональных занятий
