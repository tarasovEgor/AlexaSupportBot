import asyncio
import logging
import config

from aiogram import Bot
from aiogram import Dispatcher

from routers import router as main_router

dp = Dispatcher()

dp.include_router(main_router)


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Завершение работы...')