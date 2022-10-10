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
    def _gen_p_col(p: list):
        s = str()
        for i in p:
            s = s + i + ", "
        s = s[:-2]
        return s

    @staticmethod
    def _gen_p_val(p: list):
        s = str()
        for i in p:
            if type(i) == type(str()):
                s = s + f"\"{i}\"" + ", "
            else:
                s = s + f"{i}" + ", "
        s = s[:-2]
        return s

    @staticmethod
    def __gen_uid(tg_id: tuple):
        tg_id = list(tg_id)
        uid = []
        for i in tg_id:
            uid.append(*i)
        return uid

    async def check_user_in_db(self, msg: types.Message):
        curr = self.db.cursor()
        msg_id = str(msg.from_user.id)
        curr.execute("SELECT tg_id FROM users.students")
        tg_id = curr.fetchall()
        uid = self.__gen_uid(tg_id=tg_id)
        st = None

        for i in uid:
            if i == msg_id:
                st = True
                break
            else:
                st = False
        return st

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
