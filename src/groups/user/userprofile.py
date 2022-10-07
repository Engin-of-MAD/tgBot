from aiogram import types
from main import usr

class UserProfile:
    txt_msg = None
    usr_f_name = usr.get_first_name()
    usr_l_name = usr.get_last_name()


