from aiogram.fsm.state import StatesGroup, State


class ZammadQuery(StatesGroup):
    user_question = State()
    user_name = State()
    user_email = State()
    user_inn = State()
    user_phone_number = State()