from src.keyboards.menu_kb.menu_kb import MyKb
from main import usr

import pymysql.cursors
from aiogram import types


class MyDB:
    db = None

    def __init__(self):
        self.db = pymysql.connect(database="users",
                                  host="localhost",
                                  password="qwerty123F!",
                                  user="root")

    @staticmethod
    def _gen_p_col(self, p: list):
        s = str()
        for i in p:
            s = s + i + ", "
        s = s[:-2]
        return s

    @staticmethod
    def _gen_p_val(self, p: list):
        s = str()
        for i in p:
            if type(i) == type(str()):
                s = s + f"\"{i}\"" + ", "
            else:
                s = s + f"{i}" + ", "
        s = s[:-2]
        return s

#    @classmethod
#   def check_user_in_stud(cls, msg: types.Message):
#        curr = cls.db.cursor()
#       msg_id = msg.message_id
#        curr.execute("SELECT tg_id FROM users.students")
#        tg_id = curr.fetchall()
#        tg_id = list(tg_id)
#        print(tg_id)
#       uid = []
#        for i in tg_id:
#           uid.append(*i)
#        print(uid)
#        for i in uid:
#            if msg_id == i:
#                print("Пользователь зарегистрирован")
#                await msg.answer(text="Пожалуйста выберете пункт меню", reply_markup=await MyKb().main_menu())
#                break
#            else:
#                await msg.answer(text=usr.q_txt[0], reply_markup=await usr.auth_kb())

    @classmethod
    async def insert_to_stud(cls, **kwargs):
        curr = cls.db.cursor()
        colums: list = list()
        values: list = list()
        for key in kwargs:
            values.append(kwargs[key])
            colums.append(key)
        col = cls.gen_p_col(colums)
        val = cls.gen_p_val(values)
        curr.execute(f"INSERT students({col}) VALUES({val})")
        cls.db.commit()
