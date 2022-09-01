from keyboards.menu_kb.di_kb import yn_kb
from inline.call_data import auth_data, fio_data

from aiogram.dispatcher import FSMContext
from aiogram import types


class User:
    first_name: str = ""
    last_name: str = ""
    tg_name: str = ""
    name_user: str = ""

    date_reg: str = ""
    greeting_msg = False
    q_txt = ["Вы первый раз тут?",
             "Введите Фамилию и Имя:",
             "Пожалуйста укажите своего преподавателя:",
             "Пожалуйста укажите номер телефона"]

    async def init_user(self):
        pass

    async def auth_kb(self) -> None:
        q1_kb = await yn_kb(auth_data)
        return q1_kb
