from aiogram.dispatcher.filters.state import State, StatesGroup


class Usr(StatesGroup):
    fio = State()
    f_name = State()
    l_name = State()
    phone = State()




