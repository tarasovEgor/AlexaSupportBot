from aiogram import types, Router, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.utils import markdown
from aiogram.fsm.context import FSMContext

from states.is_client_states import IsClientQuery

from utils.gptlib import gpt4
from utils.validators import validate_email_address

router = Router(name=__name__)


async def handle_is_client(message: types.Message, state: FSMContext):
    await state.set_state(IsClientQuery.full_name)
    await message.answer(
        "Отлично, для продолжения необходимо ответить на пару вопросов 🙂\n\n"
        "✍️ Пожалуйста, назовите ваши ФИО:"
    )


@router.message(IsClientQuery.full_name, F.text)
async def handle_full_name(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await state.set_state(IsClientQuery.company_name)
    await message.answer("🏭 Название вашей компании:")


@router.message(IsClientQuery.full_name)
async def handle_invalid_full_name(message: types.Message):
    await message.answer(
        "Не разобрала, повторите, пожалуйста.. 🙃"
    )


@router.message(IsClientQuery.company_name, F.text)
async def handle_company_name(message: types.Message, state: FSMContext):
    await state.update_data(company_name=message.text)
    await state.set_state(IsClientQuery.email)
    await message.answer("📭 Адрес электронной почты:")


@router.message(IsClientQuery.company_name)
async def handle_invalid_company_name(message: types.Message):
    await message.answer(
        "Не разобрала, повторите, пожалуйста.. 🙃"
    )


@router.message(IsClientQuery.email, validate_email_address)
async def handle_user_email(
    message: types.Message,
    state: FSMContext,
    email: str
):
    await state.update_data(email=email)
    await state.set_state(IsClientQuery.inn)
    await message.answer(
        "⭐️ ИНН компании:"
    )


@router.message(IsClientQuery.email)
async def handle_invalid_user_email(message: types.Message):
    await message.answer(
        "Неверный адрес, повторите, пожалуйста.. 🙄"
    )


@router.message(IsClientQuery.inn, F.text)
async def handle_inn(message: types.Message, state: FSMContext):
    # check if the client record exists in the db 
    # if !is_client then suggest becoming a new customer
    # if is_client then continue
    await state.update_data(inn=message.text)
    await state.set_state(IsClientQuery.phone_number)
    await message.answer(
        "☎️ Номер телефона:"
    )


@router.message(IsClientQuery.inn)
async def handle_invalid_inn(message: types.Message):
    await message.answer(
        "Не разобрала, повторите, пожалуйста.. 🙃"
    )


@router.message(IsClientQuery.phone_number, F.text)
async def handle_phone_number(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    await state.set_state(IsClientQuery.question)
    await message.answer(
        "🧐 Супер! Опишите вашу проблему, я постараюсь найти решение:"
    )


@router.message(IsClientQuery.phone_number)
async def handle_invalid_phone_number(message: types.Message):
    await message.answer(
        "Не разобрала, повторите, пожалуйста.. 🙃"
    )

# here the data is being written to the db
# once the user record exists within the db they can use the alexa_gpt func

@router.message(IsClientQuery.question, F.text)
async def handle_question(message: types.Message, state: FSMContext):
    user_data = await state.update_data(question=message.text)
    await message.answer(
        "💡Обрабатываю вопрос ... \n" 
    )
    response = await gpt4(user_data['question'])
    await message.answer(
        response.choices[0].message.content
    )
    text = markdown.text(
        "Понравился ли вам ответ? 🙄\nНапишите",
        markdown.markdown_decoration.bold(markdown.text("да")),
        "или",
        markdown.markdown_decoration.bold(markdown.text("нет")),
        ":"
    )
    await message.answer(
        text=text,
        parse_mode=ParseMode.MARKDOWN_V2
    )
    await state.set_state(IsClientQuery.user_is_satisfied)


@router.message(IsClientQuery.user_is_satisfied, F.text)
async def handle_user_is_satisfied(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        await message.answer("Бала рада помочь, обращайтесь еще! 🥰\n")
        await state.clear()
    elif message.text.lower() == "нет":
        await state.set_state(IsClientQuery.has_contancted_support)
        text = markdown.text(
            "Давайте попробуем еще раз\, если ответ все еще не удовлетворительный\, то лучше обратиться в ",
            markdown.markdown_decoration.bold(
                markdown.text(
                    "службу поддержки\. 🔧\n\n📍Задать вопрос Алексе \- /ask\_alexa\n📍Написать в поддержку \- /support\n"
                )
            ),
            sep="\n"
        )
        await message.answer(
            text=text,
            parse_mode=ParseMode.MARKDOWN_V2
        )
    else:
        text = markdown.text(
            "Пожалуйста, укажите",
            markdown.markdown_decoration.bold(markdown.text("да")),
            "или",
            markdown.markdown_decoration.bold(markdown.text("нет 🙃"))
        )
        await message.answer(
            text=text,
            parse_mode=ParseMode.MARKDOWN_V2
        )


# @router.message(IsClientQuery.has_contancted_support, F.text)
# async def handle_has_contacted_support(message: types.Message, state: FSMContext):
#     if message.text == "/support":
#         user_data = await state.update_data(has_contacted_support=message.text)
#         message.answer("you have decided to contact the support line")

        
    



# await message.answer(
#         "💡Обрабатываю вопрос ... \n" 
#     )
#     response = await gpt4(message.text)
#     await message.answer(
#         response.choices[0].message.content
#     )
#     text = markdown.text(
#         "Понравился ли вам ответ? 🙄\nНапишите",
#         markdown.markdown_decoration.bold(markdown.text("да")),
#         "или",
#         markdown.markdown_decoration.bold(markdown.text("нет")),
#         ":"
#     )
#     await message.answer(
#         text=text,
#         parse_mode=ParseMode.MARKDOWN_V2
#     )
#     await state.set_state(GPTQuery.user_is_satisfied)