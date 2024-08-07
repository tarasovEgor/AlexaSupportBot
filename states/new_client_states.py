from aiogram.fsm.state import StatesGroup, State

class NewClientInfrastructureQuery(StatesGroup):
    PC_count = State()
    server_count = State()
    office_count = State()
    consent_recieved = State()
    program_type = State()


class NewClientInfoQuery(StatesGroup):
    city = State()
    company_name = State()
    company_address = State()
    phone_number = State()
    inn = State()