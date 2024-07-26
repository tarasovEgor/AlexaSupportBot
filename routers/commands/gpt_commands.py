from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.utils import markdown
from aiogram.fsm.context import FSMContext

from gptfiles.gptlib import gpt4

from states.gpt_states import GPTQuery


router = Router(name=__name__)

@router.message(Command("ask_gpt"))
async def handle_ask_gpt(message: types.Message, state: FSMContext):
    await state.set_state(GPTQuery.user_question)
    await message.answer(
        "✏️Пожалуйтста, опишите возникшую проблему: \n"
    )


@router.message(GPTQuery.user_question, F.text)
async def handle_gptquery_user_question(message: types.Message, state: FSMContext):
    await message.answer(
        "💡Обрабатываю вопрос ... \n" 
    )
    response = await gpt4(message.text)
    await message.answer(
        response.choices[0].message.content
    )
    await state.clear()