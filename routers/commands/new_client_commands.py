from aiogram import types, Router, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.utils import markdown
from aiogram.fsm.context import FSMContext

from states.new_client_states import NewClientInfrastructureQuery

from utils.plancalc import calculate_plan_price

router = Router(name=__name__)


async def handle_new_client(message: types.Message, state: FSMContext):
    await state.set_state(NewClientInfrastructureQuery.PC_count)
    await message.answer(
        "Поняла, готова сформировать для вас стоимость абонентской "
        "оплаты и направить информацию нашим специалистам для дальнейшей связи. 🙂\n\n"
        "🖥️ Подскажите, сколько у вас ПК?"
    )


@router.message(NewClientInfrastructureQuery.PC_count, F.text)
async def handle_PC_count(message: types.Message, state: FSMContext):
    if '-' in message.text[0]:
        await message.answer("Количество не может быть отрицательным.. 🙄")
    elif not message.text.isdigit():
        await message.answer("Пожалуйста, введите число. 🙃")
    else:
        await state.update_data(PC_count=message.text)
        await state.set_state(NewClientInfrastructureQuery.server_count)
        await message.answer("💽 Количество серверов?")


@router.message(NewClientInfrastructureQuery.PC_count)
async def handle_invalid_PC_count(message: types.Message):
    await message.answer(
        "Не разобрала, повторите, пожалуйста.. 🙃"
    )


@router.message(NewClientInfrastructureQuery.server_count, F.text)
async def handle_server_count(message: types.Message, state: FSMContext):
    if '-' in message.text[0]:
        await message.answer("Количество не может быть отрицательным.. 🙄")
    elif not message.text.isdigit():
        await message.answer("Пожалуйста, введите число. 🙃")
    else:
        await state.update_data(server_count=message.text)
        await state.set_state(NewClientInfrastructureQuery.office_count)
        await message.answer("🏢 Количество офисов?")


@router.message(NewClientInfrastructureQuery.server_count)
async def handle_invalid_server_count(message: types.Message):
    await message.answer(
        "Не разобрала, повторите, пожалуйста.. 🙃"
    )


@router.message(NewClientInfrastructureQuery.office_count, F.text)
async def handle_office_count(message: types.Message, state: FSMContext):
    if '-' in message.text[0]:
        await message.answer("Количество не может быть отрицательным.. 🙄")
    elif not message.text.isdigit():
        await message.answer("Пожалуйста, введите число. 🙃")
    else:
        await state.update_data(office_count=message.text)
        await state.set_state(NewClientInfrastructureQuery.program_type)
        await message.answer("Выберите подходящую программу: 🗓️")
        text = markdown.text(
            "Доступные варианты:\n\n",
            markdown.markdown_decoration.bold(markdown.text("📍 1\. Программа 5x9:\n")),
            "Обслуживание с 9 до 18 часов по рабочим дням\.\n",
            markdown.markdown_decoration.bold(markdown.text("📍 2\. Программа 7x12:\n")),
            "Обслуживание с 9 до 21 часов ежедневно без выходных дней\.\n",
            markdown.markdown_decoration.bold(markdown.text("📍 3\. Программа 7x24:\n")),
            "Круглосуточное обслуживание компьютеров ежедневно без выходных дней\.\n\n"
            "Для выбора введите номер подходящей программы\. "            
        )
        await message.answer(
            text=text,
            parse_mode=ParseMode.MARKDOWN_V2
        )


@router.message(NewClientInfrastructureQuery.office_count)
async def handle_invalid_office_count(message: types.Message):
    await message.answer(
        "Не разобрала, повторите, пожалуйста.. 🙃"
    )


@router.message(NewClientInfrastructureQuery.program_type, F.text)
async def handle_program_type(message: types.Message, state: FSMContext):
    if '-' in message.text[0]:
        await message.answer("Количество не может быть отрицательным.. 🙄")
    elif not message.text.isdigit():
        await message.answer("Пожалуйста, введите число. 🙃")
    else:
        client_infrastructure_data = await state.update_data(program_type=message.text)
        await state.set_state(NewClientInfrastructureQuery.consent_recieved)
        text = markdown.text(
            markdown.markdown_decoration.bold(
                markdown.text(f"{await calculate_plan_price(client_infrastructure_data):,.0f}")
            )
        )
        await message.answer(
            "🧾 Сумма абонентской стоимости составит " + text + " руб\.",
            parse_mode=ParseMode.MARKDOWN_V2
        )
        await message.answer("Отправить заявку на оформление договора нашим специалистам? 📩")


@router.message(NewClientInfrastructureQuery.program_type)
async def handle_program_type(message: types.Message):
    await message.answer(
        "Не разобрала, повторите, пожалуйста.. 🙃"
    )


@router.message(NewClientInfrastructureQuery.consent_recieved, F.text)
async def handle_consent_recieved(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        client_infrastructure_data = await state.update_data(consent_recieved=message.text)
        # await handle_form_new_contract_data(message, data, client_infrastructure_data)
    elif message.text.lower() == "нет":
        await state.clear()
        text = markdown.text(
            "Хорошо, возможно, вам подойдут другие тарифы? 🤔\n\n"
            "Чтобы посмотреть информацию о всех тарифах введите команду \- ",
            markdown.markdown_decoration.bold(markdown.text("/get\_plans"))
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