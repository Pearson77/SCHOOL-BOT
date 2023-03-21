from aiogram import Dispatcher, Bot, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from cfg import TOKEN, ACCESS

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


def access_try(user_id):
    return 1 if user_id in ACCESS else 0


@dp.message_handler(commands=['start'])
async def start(message: types.Message) -> None:
    await message.answer(message.from_user.id)


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
