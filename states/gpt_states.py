from aiogram.fsm.state import StatesGroup, State


class GPTQuery(StatesGroup):
    user_question = State()
    user_is_satisfied = State()