from aiogram import types, Router, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.utils import markdown

from .is_client_commands import handle_is_client
from .new_client_commands import handle_new_client
from .is_client_commands import router as is_client_commands_router

# from states.is_client_states import IsClientQuery
# from states.new_client_states import NewClientQuery
from states.ask_if_client_states import AskIfClientQuery

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message, state: FSMContext):
    text = markdown.text(
        "Давайте приступим\! 👋\n\n"
        "📍Подскажите, пожалуйста, являетесь ли вы нашим клиентом?\n\n"
        "Для выбора просто напишите",
        markdown.markdown_decoration.bold(
            markdown.text(
                "да"
            )
        ),
        markdown.text(
            "/"
        ),
        markdown.markdown_decoration.bold(
            markdown.text(
                "нет\."
            )
        )
    )
    await message.answer(
        text=text,
        parse_mode=ParseMode.MARKDOWN_V2
    )
    await state.set_state(AskIfClientQuery.is_client)


@router.message(AskIfClientQuery.is_client, F.text)
async def handle_ask_if_client(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        await handle_is_client(message, state)
    elif message.text.lower() == 'нет':
        await handle_new_client(message, state)
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


@router.message(AskIfClientQuery.is_client)
async def handle_invalid_ask_if_client(message: types.Message):
    await message.answer(
        "Не разобрала, повторите, пожалуйста.. 🙃"
    )


@router .message(Command("help"))
async def handle_help(message: types.Message):
    text = markdown.text(
        markdown.text(
            "Меня зовут",
            markdown.markdown_decoration.bold(
                markdown.text(
                    "Алекса\\,"
                )
            ),
            markdown.markdown_decoration.quote(
                "я телеграм-бот, который поможет вам решить возникшую проблему.\n\nВот список моих команд:\n\n"
            ),
            markdown.markdown_decoration.bold(
                markdown.text(
                    "📍Начало работы \- /start\n",
                    "📍Задать вопрос Алексе \- /ask\_alexa\n",
                    "📍Узнать стоимость \- /ask\_plan\n",
                    "📍Написать в поддержку \- /support\n"
                )
            )
        ),
        markdown.text(
            "Для выбора, просто нажмите на нужную команду\.\n"
        ),
        sep="\n"
    )
    await message.answer(
        text=text,
        parse_mode=ParseMode.MARKDOWN_V2
    )

# --- OLD START COMMAND HANDLER ---

# @router.message(CommandStart())
# async def handle_start(message: types.Message):
#     text = markdown.text(
#         "👋 Давайте приступим\!\n",
#         markdown.markdown_decoration.bold(
#             markdown.text(
#                 "📍Задать вопрос ChatGPT \- /ask\_gpt\n📍Написать в поддержку \- /support\n"
#             )
#         ),
#         markdown.text(
#             "Для выбора, просто нажмите на нужную команду\.\n"
#         ),
#         sep="\n"
#     )
#     await message.answer(
#         text=text,
#         parse_mode=ParseMode.MARKDOWN_V2
#     )


# --- OLD HELP COMMAND HANDLER ---


# @router .message(Command("help"))
# async def handle_help(message: types.Message):
#     text = markdown.text(
#         markdown.text(
#             "Меня зовут",
#             markdown.markdown_decoration.bold(
#                 markdown.text(
#                     "Алекса\\,"
#                 )
#             ),
#             markdown.markdown_decoration.quote(
#                 "я телеграм-бот, который поможет вам решить возникшую проблему.\n\nВот список моих команд:\n\n"
#             ),
#             markdown.markdown_decoration.bold(
#                 markdown.text(
#                     "📍Начало работы \- /start\n",
#                     "📍Задать вопрос ChatGPT \- /ask\_gpt\n",
#                     "📍Написать в поддержку \- /support\n"
#                 )
#             )
#         ),
#         markdown.text(
#             "Для выбора, просто нажмите на нужную команду\.\n"
#         ),
#         sep="\n"
#     )
#     await message.answer(
#         text=text,
#         parse_mode=ParseMode.MARKDOWN_V2
#     )