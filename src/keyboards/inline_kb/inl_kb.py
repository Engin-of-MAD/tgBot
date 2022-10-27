from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from .inl_btns import Buttons
from src.callback_data.days_cb import days_data


class InlMenu:

    inl_txt = ["Пожалуйста выберите время занятия", "Пожалуйста выберите день недели занятия"]

    @classmethod
    async def grpl_time(cls):
        btn_time = Buttons().gen_time_btn(type_lesns="grpL")

        sch_kb = InlineKeyboardMarkup(row_width=2)
        sch_kb.add(*btn_time)
        return sch_kb

    #####################################################################
    # клавиатура для выбора дня недели

    @classmethod
    async def chs_aud(cls, cb: CallbackData) -> InlineKeyboardMarkup:
        auds = InlineKeyboardMarkup(row_width=1)
        aud_a = InlineKeyboardButton(text="Аудитория А", callback_data=cb.new(aud="Aud_A"))
        aud_b = InlineKeyboardButton(text="Аудитория B", callback_data=cb.new(aud="Aud_B"))
        auds.add(aud_a, aud_b)
        return auds

    @classmethod
    async def chs_day(cls, cb: CallbackData = days_data) -> InlineKeyboardMarkup:
        day_week = InlineKeyboardMarkup()
        mon_btn = InlineKeyboardButton(text="Понедельник", callback_data=cb.new(day="Mond"))
        tue_btn = InlineKeyboardButton(text="Вторник", callback_data=cb.new(day="Tue"))
        wed_btn = InlineKeyboardButton(text="Среда", callback_data=cb.new(day="Wed"))
        thu_btn = InlineKeyboardButton(text="Четверг", callback_data=cb.new(day="Thu"))
        fri_btn = InlineKeyboardButton(text="Пятница", callback_data=cb.new(day="Fri"))
        sat_btn = InlineKeyboardButton(text="Суббота", callback_data=cb.new(day="Sat"))
        sun_btn = InlineKeyboardButton(text="Воскресенье", callback_data=cb.new(day="Sun"))

        day_week.add(mon_btn, tue_btn, wed_btn, thu_btn, fri_btn, sat_btn, sun_btn)

        return day_week

    @classmethod
    async def per_time(cls) -> InlineKeyboardMarkup:
        btn_time = Buttons().gen_time_btn(type_lesns="perL")

        aud_kb = InlineKeyboardMarkup(row_width=3)
        aud_kb.add(*btn_time)

        return aud_kb

