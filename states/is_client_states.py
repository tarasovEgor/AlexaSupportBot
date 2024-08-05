from aiogram.fsm.state import StatesGroup, State

class IsClientQuery(StatesGroup):
    full_name = State()