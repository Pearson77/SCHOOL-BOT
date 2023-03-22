from aiogram import Dispatcher, Bot, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from cfg import TOKEN, COMMANDS
from funcs import Answers, Rules


bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


async def func_await(text, message) -> None:
    """На случай, если во время state вызвали другую команду"""
    if text == "/help":
        await help_text(message)
    elif text == "/cancel":
        await cancel(message)
    elif text == "/answers":
        await answers(message)
    else:
        await rules(message)


@dp.message_handler(commands=['start'])
async def start(message: types.Message) -> None:
    await message.answer(str(message.from_user.id))


@dp.message_handler(commands=['cancel'])
async def cancel(message: types.Message) -> None:
    """Отмена действия во время state и удаление кнопок"""
    await message.answer(text="Помощь по использованию бота: /help", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(commands=['help'])
async def help_text(message: types.Message):
    """Получение help-текста из файла и профилактическое удаление кнопок, если они есть"""
    help_message = open("help.txt", mode="r", encoding="utf-8").readlines()
    await message.answer(text="".join(help_message), reply_markup=types.ReplyKeyboardRemove(), parse_mode="html")


@dp.message_handler(commands=['answers'])
async def answers(message: types.Message) -> None:
    await Answers.subject.set()
    answers_keyboard = [
        [
            types.KeyboardButton(text="Русский язык"),
            types.KeyboardButton(text="Информатика")
        ]
    ]
    markup = types.ReplyKeyboardMarkup(keyboard=answers_keyboard, resize_keyboard=True)
    await message.answer(text="Выберите нужный предмет...", reply_markup=markup)


@dp.message_handler(state=Answers.subject)
async def answers2(message: types.Message, state: FSMContext) -> None:
    text = message.text
    if text in COMMANDS:
        await func_await(text, message)
        await state.finish()
    elif text in ["Русский язык", "Информатика"]:
        await Answers.subject.set()
        type_keyboard = [
            [
                types.KeyboardButton(text="По варианту"),
                types.KeyboardButton(text="По заданию")
            ]
        ]
        markup = types.ReplyKeyboardMarkup(keyboard=type_keyboard, resize_keyboard=True)
        async with state.proxy() as data:
            data['subject'] = text
            await Answers.type.set()
            await message.answer(text="Выберите тип поиска...", reply_markup=markup)
    else:
        await cancel(message)


@dp.message_handler(state=Answers.type)
async def answers3(message: types.Message, state: FSMContext) -> None:
    await Answers.type.set()
    async with state.proxy() as data:
        data['type'] = message.text
        await Answers.request.set()
        await message.answer(text="Укажите номер варианта/задания...", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=Answers.request)
async def answers4(message: types.Message, state: FSMContext) -> None:
    await Answers.request.set()
    async with state.proxy() as data:
        data['request'] = message.text
        subject, find_type, number = data['subject'], data['type'], int(data['request'])
        await state.finish()
        await message.answer(f"Предмет: {subject}\nТип поиска: {find_type}\nНомер: {number}")


@dp.message_handler(commands=['rules'])
async def rules(message: types.Message) -> None:
    await Rules.subject.set()
    rules_keyboard = [
        [
            types.KeyboardButton(text="Русский язык"),
            types.KeyboardButton(text="Математика")
        ]
    ]
    markup = types.ReplyKeyboardMarkup(keyboard=rules_keyboard, resize_keyboard=True)
    await message.answer(text="Выберите нужный предмет...", reply_markup=markup)


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
