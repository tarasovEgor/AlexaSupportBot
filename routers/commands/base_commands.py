from aiogram import types, Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown


router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message):
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