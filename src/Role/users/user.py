from src.keyboards.inline_kb.di_kb import yn_kb
from src.callback_data.auth_cb import auth_data
from src.db.db import MyDB
from src.keyboards.menu_kb.menu_kb import MyKb
from src.fsm.user_fsm import Usr


from aiogram import types


class User:
    #########################################################################
    # variables

    first_name: str = None
    last_name: str = None
    phone_num = None
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

    @classmethod
    async def show_profile(cls, msg: types.Message) -> None:
        f_n = cls.first_name
        l_n = cls.last_name
        u_n = cls.tg_nickname
        phone = cls.phone_num
        tg_id = cls.tg_id
        role = cls.role
        txt_profile = f"Ваш профиль:\n" \
                      f"Имя: {f_n}\n" \
                      f"Фамилия: {l_n}\n" \
                      f"Роль: {role}\n"\
                      f"User_id: {tg_id}\n" \
                      f"User_nickname: {u_n}\n" \
                      f"User_phone: {phone}"
        await msg.answer(txt_profile)

    #########################################################################
    # setters
    @classmethod
    def set_userdata(cls, msg):
        user_data = MyDB().getdata_stud(msg)
        cls.first_name = user_data["First_name"]
        cls.last_name = user_data["Last_name"]
        cls.phone_num = user_data["phone"]
        cls.tg_id = user_data["tg_id"]
        cls.tg_nickname = user_data["tg_name"]

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
        chk_u = await MyDB().check_user_in_db(msg)
        if chk_u:
            await msg.answer(text=MyKb().m_txt[0], reply_markup=await MyKb().main_menu())
        else:
            await msg.answer(text=User().q_txt[1])
            await Usr.f_name.set()
