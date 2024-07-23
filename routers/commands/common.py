from aiogram import Router, types
from aiogram.utils import markdown
from aiogram.enums import ParseMode


router = Router(name=__name__)

@router.message()
async def handle_common_messages(message: types.Message):
    if message.text:
        text = markdown.text(
            "Не совсем поняла вас\.\. 🙃\nВот список того\, что я пока что умею:\n",
            markdown.markdown_decoration.bold(
                markdown.text(
                    "\n📍Задать вопрос ChatGPT \- /ask\_gpt\n📍Написать в поддержку \- /support\n"
                    )
                )
        )
        await message.answer(
            text=text,
            parse_mode=ParseMode.MARKDOWN_V2
        )
    else:
        text = markdown.text(
            "Такого я пока что не умею\.\. 😞\n\nДля описания доступных функций воспользуйтесь командой \- ",
            markdown.markdown_decoration.bold(
            markdown.text(
                "/help"
                )
            )
        )
        await message.answer(
            text=text,
            parse_mode=ParseMode.MARKDOWN_V2
        )