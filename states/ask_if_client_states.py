from aiogram.fsm.state import StatesGroup, State

class AskIfClientQuery(StatesGroup):
    is_client = State()