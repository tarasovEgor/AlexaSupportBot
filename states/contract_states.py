from aiogram.fsm.state import StatesGroup, State

class ContractDataQuery(StatesGroup):
    full_name = State()
    city = State()
    company_name = State()
    company_address = State()
    phone_number = State()
    email = State()
    inn = State()