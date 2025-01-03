from aiogram.fsm.state import StatesGroup, State


class BookStates(StatesGroup):
    series = State()
    book_name = State()