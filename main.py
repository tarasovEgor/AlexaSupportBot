import asyncio
import logging
import config

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import CommandStart, Command


# BOT_TOKEN = "7355417367:AAEvTenRqpck40AxxNNQ1FTIjpFylZfFAmI"

dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    text = """
        - Для получения ответа от ChatGPT, введите команду /gpt \n\n- Для формирования заявки в поддержку, введите команду /support
    """
    await message.answer(text=text)



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

