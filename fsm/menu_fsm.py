from aiogram.dispatcher.filters.state import State, StatesGroup


class MenuCtrl(StatesGroup):
    menu_sch = State()
    menu_aud = State()
    menu_info = State()
    menu_switch = State()