import pymysql
from aiogram import types
from pymysql.cursors import DictCursor

from .db import MyDB


class StudDB(MyDB):

    async def check_user_in_db(self, msg: types.Message):
        curr = self.db.cursor()
        msg_id = str(msg.from_user.id)
        curr.execute("SELECT tg_id FROM users.students")
        tg_id = dict(*curr.fetchall())
        state = None
        for uid in tg_id:
            if msg_id == tg_id[uid]:
                state = True
            else:
                state = False
        return state

    def __init__(self):
       self.db = pymysql.connect(database="users",
                                  cursorclass=DictCursor,
                                  host="localhost",
                                  password="qwerty123F!",
                                  user="root")

    def get_from_db(self, uid: int = None):
        sql_q = None
        if uid != None:
            uid = str(uid)
            sql_q = f"SELECT * FROM users.students WHERE tg_id = \'{uid}\'"
        curr = self.db.cursor()
        curr.execute(sql_q)
        u_data = curr.fetchall()
        u_data = dict(*u_data)

        if self.check_null(u_data):
            u_data = dict(First_Name=None,
                          Last_Name=None,
                          phone_number=None,
                          role_user=None,
                          tg_id=None,
                          tg_username=None)
        return u_data

    def send_to_db(self, **kwargs):
        curr = self.db.cursor()
        colums: list = list()
        values: list = list()
        for key in kwargs:
            values.append(kwargs[key])
            colums.append(key)
        col = self._gen_p_col(colums)
        val = self._gen_p_val(values)
        curr.execute(f"INSERT students({col}) VALUES({val})")
        self.db.commit()
