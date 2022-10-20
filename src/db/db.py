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
    def check_null(lst: list):
        if len(lst) == 0:
            return False
        else:
            return True

    @staticmethod
    def convert_to_list(*tup: tuple):
        tup = list(*tup)
        un_pack = list()
        for i in tup:
            un_pack.append(i)
        return un_pack

    def getdata_stud(self, msg: types.Message):
        tg_id = str(msg.from_user.id)
        sql_q = f"SELECT * FROM users.students WHERE tg_id = \'{tg_id}\'"
        curr = self.db.cursor()
        curr.execute(sql_q)
        u_data = curr.fetchall()
        u_d = self.convert_to_list(*u_data)
        check = self.check_null(u_d)
        if check:
            mydata = dict(First_name=u_d[1],
                          Last_name=u_d[2],
                          phone=u_d[3],
                          role_user=u_d[4],
                          tg_id=u_d[5],
                          tg_name=u_d[6])
            return mydata
        else:
            print("Извините, пользователя нет в базе данных или она пуста")
            mydata = dict(First_name=None,
                          Last_name=None,
                          phone=None,
                          role_user=None,
                          tg_id=None,
                          tg_name=None)
            return mydata

    @staticmethod
    def _gen_p_col(p: list):
        s = str()
        for i in p:
            s = s + i + ", "
        s = s[:-2]
        return s

    @staticmethod
    def _gen_p_val(p: list):
        s = ""
        for i in p:
            if isinstance(i, str):
                s = s + f"\"{i}\"" + ", "
            else:
                s = s + f"{i}" + ", "
        s = s[:-2]
        return s

    @staticmethod
    def __convert_data(tup: tuple):
        tup = list(tup)
        uid = []
        for i in tup:
            uid.append(*i)
        return uid

    async def check_user_in_db(self, msg: types.Message):
        curr = self.db.cursor()
        msg_id = str(msg.from_user.id)
        curr.execute("SELECT tg_id FROM users.students")
        tg_id = curr.fetchall()
        uid = self.__convert_data(tup=tg_id)
        st = None

        for i in uid:
            if i == msg_id:
                st = True
                break
            else:
                st = False
        return st

    async def insert_to_stud(self, **kwargs):
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
