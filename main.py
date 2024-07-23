import asyncio
import logging
import config

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown
from aiogram.enums import ParseMode 

dp = Dispatcher()

@dp.message(CommandStart())
async def handle_start(message: types.Message):
    text = markdown.text(
        "👋 Давайте приступим\! Как я могу вам помочь?\n",
        markdown.markdown_decoration.bold(
            markdown.text(
                "📍Задать вопрос ChatGPT \- /ask\_gpt\n📍Написать в поддержку \- /support\n"
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


@dp.message(Command("help"))
async def hndle_help(message: types.Message):
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
                    "📍Задать вопрос ChatGPT \- /ask\_gpt\n",
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


# @dp.message()
# async def echo_message(message: types.Message):
#     if message.text:
#         await message.answer(text="Hello there!")
    # await message.answer(message.text)


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

