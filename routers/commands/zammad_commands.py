from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from utils.zammadlib import submit_to_zammad
from utils.validators import validate_email_address

from states.zammad_states import ZammadQuery


router = Router(name=__name__)


@router.message(Command("support"))
async def handle_support(message: types.Message, state: FSMContext):
    await state.set_state(ZammadQuery.user_question)
    await message.answer(
         "✏️Пожалуйтста, опишите возникшую проблему: \n"
    )


@router.message(ZammadQuery.user_question, F.text)
async def handle_user_question(message: types.Message, state: FSMContext):
    await state.update_data(user_question=message.text)
    await state.set_state(ZammadQuery.user_name)
    await message.answer(
         "📋 Отлично, как можно к вам обращаться? \n"
    )


@router.message(ZammadQuery.user_question)
async def handle_invalid_user_question(message: types.Message):
    await message.answer(
        "Не разобрала, пожалуйста, повторите вопрос.. 🙃"
    )


@router.message(ZammadQuery.user_name, F.text)
async def handle_user_name(message: types.Message, state: FSMContext):
    await state.update_data(user_name=message.text)
    await state.set_state(ZammadQuery.user_email)
    await message.answer(
        f"📭 Очень приятно, {message.text}! "
        "Назовите ваш адрес эл. почты:"
    )


@router.message(ZammadQuery.user_name)
async def handle_invalid_user_name(message: types.Message):
    await message.answer(
        "Не разобрала, повторите, пожалуйста.. 🙃"
    )


@router.message(ZammadQuery.user_email, validate_email_address)
async def handle_user_email(
    message: types.Message,
    state: FSMContext,
    email: str
):
    await state.update_data(user_email=email)
    await state.set_state(ZammadQuery.user_inn)
    await message.answer(
        "⭐️ Записала! Назовите ваш ИНН:"
    )


@router.message(ZammadQuery.user_email)
async def handle_invalid_user_email(message: types.Message):
    await message.answer(
        "Неверный адрес, повторите, пожалуйста.. 🙄"
    )
    

@router.message(ZammadQuery.user_inn, F.text)
async def handle_user_inn(message: types.Message, state: FSMContext):
    await state.update_data(user_inn=message.text)
    await state.set_state(ZammadQuery.user_phone_number)
    await message.answer(
        "☎️ Супер! Назовите ваш номер телефона:"
    )


@router.message(ZammadQuery.user_inn)
async def handle_invalid_user_inn(message: types.Message):
    await message.answer(
        "Неверный ИНН, повторите, пожалуйста.. 🙃"
    )


@router.message(ZammadQuery.user_phone_number, F.text)
async def handle_user_phone_number(message: types.Message, state: FSMContext):
    zammad_user_data = await state.update_data(user_phone_number=message.text)
    await state.clear()
    await message.answer(
        "⏳ Формирую заявку...\n"
    )
    await submit_to_zammad(zammad_user_data)
    await message.answer(
        "☺️ Заявка успешно сформирована, в ближайшее время с вами свяжется наш специалист.\n"
    )
    

@router.message(ZammadQuery.user_phone_number)
async def handle_invalid_user_phone_number(message: types.Message):
    await message.answer(
        "Неверный номер, повторите, пожалуйста.. 🙃"
    )