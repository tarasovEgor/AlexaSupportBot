from aiogram import Router, types
from aiogram.filters import Command

from gptfiles.gptlib import ask_chatGPT

router = Router(name=__name__)

@router.message(Command("ask_gpt"))
async def handle_ask_gpt(message: types.Message):
    await message.answer("✏️Пожалуйтста, опишите возникшую проблему: \n")