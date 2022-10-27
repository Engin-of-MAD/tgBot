from aiogram import types


class MyKb:

    m_txt = ["Пожалуйста выберете пункт меню",
             "Пожалуйста выберите нужный тип занятий",
             "Пожалуйста выберите нужную аудиторию",
             "Пожалуйста выберете время занятия Аудитория A",
             "Пожалуйста выберете время занятия, Аудитория B",
             "Пожалуйста выберете время персональных занятий занятий",
             "Пожалуйста выберете время групповых занятий занятий"]

    ########################################################################################
    # Кнопки

    btn_schL = types.KeyboardButton("Расписание занятий")
    btn_repA = types.KeyboardButton("Репетиционные Аудитории")
    btn_a = types.KeyboardButton("Аудитория А")
    btn_b = types.KeyboardButton("Аудитория B")
    btn_info = types.KeyboardButton("Info")
    btn_back = types.KeyboardButton("Назад")
    btn_grpL = types.KeyboardButton("Групповые Занятия")
    btn_perL = types.KeyboardButton("Индивидуальные Занятия")
    btn_bToMain = types.KeyboardButton("Вернуться в главное меню")
    btn_ph = types.KeyboardButton('Отправить свой контакт ☎️', request_contact=True)

    ######################################################################################
    # Клавиатуры
    @classmethod
    async def main_menu(cls) -> types.ReplyKeyboardMarkup:
        bs_kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        bs_kb.add(cls.btn_schL)
        bs_kb.add(cls.btn_repA)
        bs_kb.add(cls.btn_info)
        return bs_kb

    # Меню Расписания Аудиторий
    @classmethod
    async def menu_sch_aud(cls) -> types.ReplyKeyboardMarkup:
        aud_kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        aud_kb.add(cls.btn_a)
        aud_kb.add(cls.btn_b)
        aud_kb.add(cls.btn_info)
        aud_kb.add(cls.btn_back)
        return aud_kb

    # Меню расписания занятий
    @classmethod
    async def menu_sch_les(cls) -> types.ReplyKeyboardMarkup:
        les_kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        les_kb.add(cls.btn_grpL)
        les_kb.add(cls.btn_perL)
        les_kb.add(cls.btn_info)
        les_kb.add(cls.btn_bToMain)
        return les_kb

    @classmethod
    async def phone_kb(cls) -> types.ReplyKeyboardMarkup:
        ph_kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        ph_kb.add(cls.btn_ph)
        return ph_kb
