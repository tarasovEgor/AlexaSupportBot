from aiogram.fsm.state import StatesGroup, State

class NewClientQuery(StatesGroup):
    PC_count = State()
    server_count = State()
    office_count = State()