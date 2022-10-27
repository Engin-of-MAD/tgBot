import pymysql.cursors
from aiogram import types
from abc import ABC, abstractmethod


class MyDB(ABC):
    db = None

    @abstractmethod
    async def send_to_db(self, **kwargs):
        pass

    @abstractmethod
    def get_from_db(self, msg: types.Message):
        pass

    async def check_user_in_db(self, msg: types.Message):
        pass

    @staticmethod
    def check_null(lst):
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
