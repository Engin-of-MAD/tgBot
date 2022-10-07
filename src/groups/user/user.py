from src.keyboards.inline_kb.di_kb import yn_kb
from src.keyboards.inline_kb.call_data import auth_data
from aiogram import types


class User:
    #########################################################################
    # variables

    first_name: str = None
    last_name: str = None
    phone_num = None
    tg_id: int = None
    tg_nickname: str = None
    auth_user: bool = None
    date_reg: str = None
    user_data = None

    q_txt = ["Вы первый раз тут?",
             "Введите Имя:",
             "Введите Фамилию:",
             "Пожалуйста укажите номер телефона"]

    @classmethod
    async def show_profile(cls, msg: types.Message) -> None:
        f_n = cls.first_name
        l_n = cls.last_name
        u_n = cls.tg_nickname
        phone = cls.phone_num
        tg_id = cls.tg_id
        txt_profile = f"Ваш профиль:\n"\
                      f"Имя: {f_n}\n"\
                      f"Фамилия: {l_n}\n"\
                      f"User_id: {tg_id}\n"\
                      f"User_nickname: {u_n}\n" \
                      f"User_phone: {phone}"
        await msg.answer(txt_profile)

    #########################################################################
    # setters

    def set_tg_id(self, msg: types.Message) -> None:
        self.tg_id = msg.from_user.id

    def set_tg_name(self, msg: types.Message) -> None:
        self.tg_nickname = msg.from_user.username

    def set_phone(self, msg: types.Message) -> None:
        self.phone_num = msg.contact.phone_number

    #########################################################################
    # user_kb
    @staticmethod
    async def auth_kb() -> None:
        q1_kb = await yn_kb(auth_data)
        return q1_kb

    #########################################################################

    async def gen_data(self) -> dict:
        data = dict(First_Name=self.first_name,
                    Last_Name=self.last_name,
                    phone_number=self.phone_num,
                    tg_id=self.tg_id,
                    tg_username=self.tg_nickname,
                    auth_user=self.auth_user)
        return data

    #########################################################################

