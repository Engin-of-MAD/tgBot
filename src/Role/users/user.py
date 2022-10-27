from src.callback_data.auth_cb import auth_data
from src.db.stud_db import StudDB
from src.keyboards.menu_kb.menu_kb import MyKb
from src.keyboards.inline_kb.di_kb import yn_kb
from src.fsm.user_fsm import Usr
from src.db.lessons_db import LessonDb
from main import bot

from aiogram import types

lesson_db = LessonDb()


class User:
    #########################################################################
    # variables

    first_name: str = None
    last_name: str = None
    phone_num = None
    role_user = None
    tg_id: int = None
    tg_nickname: str = None
    date_reg: str = None
    user_data = None

    role = "Студент"

    q_txt = ["Вы первый раз тут?",
             "Введите Имя:",
             "Введите Фамилию:",
             "Пожалуйста укажите номер телефона",
             "Вы зарегистрированы"]

    def __init__(self, msg=None, uid=None):

        if uid != None:
            user_data = StudDB().get_from_db(uid=uid)
            # print(user_data)
            self.first_name = user_data["First_name"]
            self.last_name = user_data["Last_name"]
            self.phone_num = user_data["phone"]
            self.tg_id = user_data["tg_id"]
            self.tg_nickname = user_data["tg_name"]


    async def show_profile(self, msg: types.Message) -> None:
        f_n = self.first_name
        l_n = self.last_name
        u_n = self.tg_nickname
        phone = self.phone_num
        tg_id = self.tg_id
        role = self.role
        txt_profile = f"Ваш профиль:\n" \
                      f"Имя: {f_n}\n" \
                      f"Фамилия: {l_n}\n" \
                      f"Роль: {role}\n" \
                      f"User_id: {tg_id}\n" \
                      f"User_nickname: {u_n}\n" \
                      f"User_phone: {phone}\n"\
                      f"Занятие: {None}\n"\
                      f"Преподаватель: {None}"
        await msg.answer(txt_profile)

    async def show_lessons(self, msg: types.Message):
        db = LessonDb().get_from_db(msg)
        print(len(db))
        if len(db) == 0:
            db = {"date": None, "aud": None, "day": None}
        ls_profile = f"Время и дата занятия: {db['date']}\n" \
                     f"Аудитория занятия: {db['aud']}\n" \
                     f"День занятия: {db['day']}\n"
        await msg.answer(text=ls_profile)

    #########################################################################
    # setters
    @classmethod
    def set_userdata(cls, uid):
        user_data = StudDB().get_from_db(uid)
        print(user_data)
        cls.first_name = user_data["First_Name"]
        cls.last_name = user_data["Last_Name"]
        cls.phone_num = user_data["phone_number"]
        cls.tg_id = user_data["tg_id"]
        cls.tg_nickname = user_data["tg_username"]

    @classmethod
    def set_tg_id(cls, msg: types.Message) -> None:
        cls.tg_id = msg.from_user.id

    @classmethod
    def set_tg_name(cls, msg: types.Message) -> None:
        cls.tg_nickname = msg.from_user.username

    @classmethod
    def set_phone_num(cls, msg: types.Message) -> None:
        cls.phone_num = msg.contact.phone_number

    @classmethod
    def set_first_name(cls, data: dict):
        cls.first_name = data["f_name"]

    @classmethod
    def set_last_name(cls, data: dict):
        cls.last_name = data["l_name"]

    #########################################################################
    # user_kb
    @staticmethod
    async def auth_kb() -> None:
        q1_kb = await yn_kb(auth_data)
        return q1_kb

    #########################################################################
    @classmethod
    async def gen_data(cls) -> dict:
        data = dict(First_Name=cls.first_name,
                    Last_Name=cls.last_name,
                    phone_number=cls.phone_num,
                    tg_id=cls.tg_id,
                    tg_username=cls.tg_nickname)
        return data

    #########################################################################
    @staticmethod
    async def chk_usr(msg: types.Message) -> None:
        chk_u = await StudDB().check_user_in_db(msg)
        if chk_u:
            await msg.answer(text=MyKb().m_txt[0], reply_markup=await MyKb().main_menu())
        else:
            await msg.answer(text=User().q_txt[1])
            await Usr.f_name.set()

    async def chk_lessons(self, uid, call: types.CallbackQuery = None, msg: types.Message = None):
        chk_l = LessonDb().check_user_in_db(uid)
        if call != None and msg == None:
            if chk_l:
                await bot.edit_message_text(chat_id=call.from_user.id,
                                            message_id=call.message.message_id,
                                            text="У вас уже есть занятие")
            else:
                lesson_db.send_to_db(**lesson_db.data)

        if call == None and msg != None:
            if chk_l:
                await bot.edit_message_text(chat_id=call.from_user.id,
                                            message_id=call.message.message_id,
                                            text="У вас уже есть занятие")
            else:
                lesson_db.send_to_db(**lesson_db.data)
