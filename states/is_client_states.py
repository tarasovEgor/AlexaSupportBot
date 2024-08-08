from aiogram.fsm.state import StatesGroup, State

class IsClientQuery(StatesGroup):
    full_name = State()
    company_name = State()
    email = State()
    phone_number = State()
    inn = State()
    question = State()
    user_is_satisfied = State()
    has_contancted_support = State()