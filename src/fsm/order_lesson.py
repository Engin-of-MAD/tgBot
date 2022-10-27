from aiogram.dispatcher.filters.state import State, StatesGroup


class OrderLesson(StatesGroup):
    aud_a = State()
    aud_b = State()
    day = State()
    time = State()
