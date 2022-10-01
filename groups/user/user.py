from keyboards.inline_kb.di_kb import yn_kb
from keyboards.inline_kb.call_data import auth_data
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

    async def show_profile(self, msg: types.Message):

        u_n = self.get_tg_name()
        phone = self.get_phone_num()
        tg_id = self.get_tg_id()
        txt_profile = f"Ваш профиль:\n"\
                      f"Имя: {self.first_name}\n"\
                      f"Фамилия: {self.last_name}\n"\
                      f"User_id: {tg_id}\n"\
                      f"User_nickname: {u_n}\n" \
                      f"User_phone: {phone}"
        await msg.answer(txt_profile)

    #########################################################################
    # setters
    def set_auth_user(self, auth):
        self.auth_user = auth

    def set_first_name(self, f_name):
        self.first_name = f_name
        print(f_name)

    def set_last_name(self, l_name):
        self.first_name = l_name
        print(l_name)

    def set_tg_id(self, msg: types.Message):
        self.tg_id = msg.from_user.id

    def set_tg_name(self, msg: types.Message):
        self.tg_nickname = msg.from_user.username

    def set_phone(self, msg: types.Message):
        self.phone_num = msg

    def set_data(self, data):
        self.user_data = data

        self.set_first_name(data["f_name"])
        self.set_last_name(data['l_name'])

    #########################################################################
    # getters
    def get_data(self):
        print(self.user_data)

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_tg_id(self):
        return self.tg_id

    def get_tg_name(self):
        return self.tg_nickname

    def get_phone_num(self):
        return self.phone_num
    #########################################################################
    # user_kb

    async def auth_kb(self) -> None:
        q1_kb = await yn_kb(auth_data)
        return q1_kb

    #########################################################################

    async def gen_data(self) -> dict:
        data = dict(First_Name=self.first_name,
                    Last_Name=self.last_name,
                    phone_number=self.phone_num,
                    auth_user=self.auth_user,
                    tg_id=self.tg_id,
                    tg_username=self.tg_nickname)
        return data

    #########################################################################

