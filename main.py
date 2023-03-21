from aiogram import Dispatcher, Bot, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

from cfg import TOKEN, ACCESS

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


def access_try(user_id):
    return 1 if user_id in ACCESS else 0


@dp.message_handler(commands=['start'])
async def start(message: types.Message) -> None:
    await message.answer(message.from_user.id)


@dp.message_handler(commands=['cancel'])
async def cancel(message: types.Message) -> None:
    await message.answer(text="Помощь по использованию бота: /help", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(commands=['help'])
async def help_text(message: types.Message):
    help_message = open("help.txt", mode="r", encoding="utf-8").readlines()
    await message.answer("".join(help_message), parse_mode="html")


@dp.message_handler(commands=['answers'])
async def answers(message: types.Message) -> None:
    answers_keyboard = [
        [
            types.KeyboardButton(text="Русский язык"),
            types.KeyboardButton(text="Информатика")
        ]
    ]
    markup = types.ReplyKeyboardMarkup(keyboard=answers_keyboard, resize_keyboard=True)
    await message.answer(text="Выберите нужный предмет...", reply_markup=markup)


@dp.message_handler(commands=['rules'])
async def rules(message: types.Message) -> None:
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
