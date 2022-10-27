import pymysql
from aiogram import types
from pymysql.cursors import DictCursor
from .db import MyDB


class LessonDb(MyDB):

    data = {}

    def __init__(self):
        self.db = pymysql.connect(database='schedule',
                                  host="localhost",
                                  password="qwerty123F!",
                                  user="root",
                                  cursorclass=DictCursor)

    def get_from_db(self, msg: types.Message):
        msg_id = msg.from_user.id
        print(msg_id)
        sql_q = f"SELECT * FROM week_schedule WHERE st_tg_id = \'{msg_id}\'"
        curr = self.db.cursor()
        curr.execute(sql_q)
        u_data = curr.fetchall()
        u_data = dict(*u_data)
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
        curr.execute(f"INSERT week_schedule({col}) VALUES({val})")
        self.db.commit()

    def check_user_in_db(self, msg: int = None):
        uid = str(msg)

        sql_q = f"SELECT st_tg_id FROM week_schedule WHERE st_tg_id = {uid}"

        curr = self.db.cursor()
        curr.execute(sql_q)
        db = curr.fetchall()
        db = dict(*db)
        state = None

        for key in db:
            if uid == db[key]:
                state = True
            else:
                state = False
        return state
