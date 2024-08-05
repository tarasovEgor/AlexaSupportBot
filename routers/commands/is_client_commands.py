from aiogram import types, Router, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.utils import markdown
from aiogram.fsm.context import FSMContext

from states.is_client_states import IsClientQuery


router = Router(name=__name__)


@router.message(IsClientQuery.full_name, F.text)
async def handle_is_client(message: types.Message, state: FSMContext):
    await message.answer(
        "вы клиент"
    )