from aiogram.types import InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from src.callback_data.time_cb import time_data


class Buttons:

    @classmethod
    def gen_time_btn(cls, get_data: list = [], type_lesns="perL", cb: CallbackData = time_data):
        # Часы
        h = 11
        # Минуты
        m = "00"
        btn_time = []

        if "perL" == type_lesns:
            if 0 == len(get_data):
                for i in range(11):
                    btn_time.append(InlineKeyboardButton(text=f'{h}:{m}', callback_data=cb.new(time=f"btn{i}p")))

                    h += 1

            return btn_time

        elif "grpL" == type_lesns:
            if 0 == len(get_data):
                for i in range(6):
                    btn_time.append(InlineKeyboardButton(text=f'{h}:{m}', callback_data=cb.new(time=f"btn{i}g")))
                    h += 2

            return btn_time
