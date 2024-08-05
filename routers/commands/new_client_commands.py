from aiogram import types, Router, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.utils import markdown
from aiogram.fsm.context import FSMContext

from states.new_client_states import NewClientQuery


router = Router(name=__name__)


@router.message(NewClientQuery.PC_count, F.text)
async def handle_new_client(message: types.Message, state: FSMContext):
    await message.answer(
        "вы не клиент"
    )