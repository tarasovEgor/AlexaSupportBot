from aiogram import types, Router, F
from aiogram.enums import ParseMode
from aiogram.utils import markdown
from aiogram.fsm.context import FSMContext

from states.contract_states import ContractDataQuery

from utils.validators import validate_email_address

router = Router(name=__name__)


async def handle_form_new_contract(message: types.Message, state: FSMContext, client_infrastructure_data: dict):
    await state.set_state(ContractDataQuery.full_name)
    await message.answer(
        "⭐️ Отлично! Для связи со специалистом, мне необходимо узнать еще пару моментов.\n\n"
        "📝 Подскажите, пожалуйста, как вас зовут? (ФИО)"
    )


@router.message(ContractDataQuery.full_name, F.text)
async def handle_full_name(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await state.set_state(ContractDataQuery.city)
    await message.answer(
        "🌆 В каком городе находится ваша компания?"
    )


@router.message(ContractDataQuery.full_name)
async def handle_invalid_full_name(message: types.Message, state: FSMContext):
    await message.answer(
        "Не разобрала, повторите, пожалуйста.. 🙃"
    )


@router.message(ContractDataQuery.city, F.text)
async def handle_city(message: types.Message, state: FSMContext):
    await state.update_data(city=message.text)
    await state.set_state(ContractDataQuery.company_name)
    await message.answer(
        "🏢 Название компании?"
    )


@router.message(ContractDataQuery.city)
async def handle_invalid_city(message: types.Message):
    await message.answer(
        "Не разобрала, повторите, пожалуйста.. 🙃"
    )


@router.message(ContractDataQuery.company_name, F.text)
async def handle_company_name(message: types.Message, state: FSMContext):
    await state.update_data(company_name=message.text)
    await state.set_state(ContractDataQuery.company_address)
    await message.answer(
        "📇 Адрес компании?"
    )


@router.message(ContractDataQuery.company_name)
async def handle_invalid_company_name(message: types.Message):
    await message.answer(
        "Не разобрала, повторите, пожалуйста.. 🙃"
    )


@router.message(ContractDataQuery.company_address, F.text)
async def handle_company_address(message: types.Message, state: FSMContext):
    await state.update_data(company_address=message.text)
    await state.set_state(ContractDataQuery.inn)
    await message.answer(
        "📑 ИНН компании?"
    )


@router.message(ContractDataQuery.company_address)
async def handle_invalid_company_address(message: types.Message):
    await message.answer(
        "Не разобрала, повторите, пожалуйста.. 🙃"
    )


@router.message(ContractDataQuery.inn, F.text)
async def handle_inn(message: types.Message, state: FSMContext):
    await state.update_data(inn=message.text)
    await state.set_state(ContractDataQuery.phone_number)
    await message.answer(
        "📞 Ваш номер телефона?"
    )


@router.message(ContractDataQuery.inn)
async def handle_invalid_inn(message: types.Message):
    await message.answer(
        "Не разобрала, повторите, пожалуйста.. 🙃"
    )


@router.message(ContractDataQuery.phone_number, F.text)
async def handle_phone_number(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    await state.set_state(ContractDataQuery.email)
    await message.answer(
        "📧 Ваш адрес эл. почты?"
    )


@router.message(ContractDataQuery.phone_number)
async def handle_invalid_phone_number(message: types.Message):
    await message.answer(
        "Не разобрала, повторите, пожалуйста.. 🙃"
    )


@router.message(ContractDataQuery.email, validate_email_address)
async def handle_email(message: types.Message, state: FSMContext, email: str):
    contract_data = await state.update_data(email=email)
    await state.clear()

    # to_user_info model ...
    # write to db ...
    # send via email

    await message.answer(
        "😇 Отлично, спасибо! Информация направлена нашим специалистам, свяжемся с вами в ближайщее время."
    )

@router.message(ContractDataQuery.email)
async def handle_invalid_email(message: types.Message, state: FSMContext):
    await message.answer(
        "Неверный адрес, повторите, пожалуйста.. 🙄"
    )