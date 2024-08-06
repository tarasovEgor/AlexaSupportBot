from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext

from utils.gptlib import gpt4

from states.gpt_states import GPTQuery

router = Router(name=__name__)


@router.message(Command("ask_alexa"))
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
    text = markdown.text(
        "Понравился ли вам ответ? 🙄\nНапишите",
        markdown.markdown_decoration.bold(markdown.text("да")),
        "или",
        markdown.markdown_decoration.bold(markdown.text("нет")),
        ":"
    )
    await message.answer(
        text=text,
        parse_mode=ParseMode.MARKDOWN_V2
    )
    await state.set_state(GPTQuery.user_is_satisfied)


@router.message(GPTQuery.user_question)
async def handle_gptquery_invalid_user_question(message: types.Message):
    await message.answer(
        "Извините, не совсем поняла ваш вопрос.. 🙃\n"
    )


@router.message(GPTQuery.user_is_satisfied, F.text)
async def handle_is_satisfied(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        await message.answer("Бала рада помочь, обращайтесь еще! 🥰\n")
        await state.clear()
    elif message.text.lower() == "нет":
        text = markdown.text(
            "Давайте попробуем еще раз\, если ответ все еще не удовлетворительный\, то лучше обратиться в нашу ",
            markdown.markdown_decoration.bold(
                markdown.text(
                    "службу поддержки\. 🔧\n\n📍Задать вопрос Алексе \- /ask\_alexa\n📍Написать в поддержку \- /support\n"
                )
            ),
            sep="\n"
        )
        await message.answer(
            text=text,
            parse_mode=ParseMode.MARKDOWN_V2
        )
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