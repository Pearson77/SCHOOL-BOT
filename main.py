from aiogram import Dispatcher, Bot, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor

from cfg import TOKEN, COMMANDS
from funcs import Answers, Rules
from inf import I2,I5,I6,I8,I12,I14,I15,I16,I17,I19,I20,I21,I23,I24,I25
from Math import M1,M2,M3,M4,M5,M6,M7,M8,M9,M10,M11
#from Rus import

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
    await message.reply(str(message.chat.type))


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

########################################################################################################################
@dp.message_handler(commands=['rules'])
async def rules(message: types.Message) -> None:
    await Rules.subject.set()
    rules_keyboard = [
        [
            types.KeyboardButton(text="Русский язык"),
            types.KeyboardButton(text="Математика"),
            types.KeyboardButton(text="Информатика")
        ]
    ]
    markup = types.ReplyKeyboardMarkup(keyboard=rules_keyboard, resize_keyboard=True)
    await message.answer(text="Выберите нужный предмет...", reply_markup=markup)


@dp.message_handler(state=Rules.subject)
async def rules2(message: types.Message, state: FSMContext) -> None:
    text = message.text
    if text in COMMANDS:
        await func_await(text, message)
        await state.finish()
    elif text in ["Русский язык", "Математика","Информатика"]:
        await Rules.subject.set()


        if text in ["Русский язык"]:
            async with state.proxy() as data1:
                data1['type'] = message.text
                await Rules.request.set()
                await message.answer(text="Укажите номер задания с 1 по 27", reply_markup=types.ReplyKeyboardRemove())

            @dp.message_handler(state=Rules.request)
            async def rules2v1(message: types.Message, state: FSMContext) -> None:
                await Rules.request.set()
                async with state.proxy() as data1:
                    data1['request'] = message.text
                    number = int(data1['request'])
                    await state.finish()
                    if number >= 1 and number <= 27:
                        await message.answer(f"Номер: {number}")
                    else:
                        await message.answer(f"Задания с таким номером не существует :(")


        elif text in ["Математика"]:
            async with state.proxy() as data2:
                await Rules.request.set()
                await message.answer(text="Укажите номер задания с 1 по 11", reply_markup=types.ReplyKeyboardRemove())

            @dp.message_handler(state=Rules.request)
            async def rules2v2(message: types.Message, state: FSMContext) -> None:
                await Rules.request.set()
                async with state.proxy() as data2:
                    data2['request'] = message.text
                    number2 = int(data2['request'])
                    await state.finish()
                    if number2 >= 1 and number2 <= 11:
                        if number2==1:
                            await message.answer(M1)
                        if number2==2:
                            await message.answer(M2)
                        if number2==3:
                            await message.answer(M3)
                        if number2==4:
                            await message.answer(M4)
                        if number2==5:
                            await message.answer(M5)
                        if number2==6:
                            await message.answer(M6)
                        if number2==7:
                            await message.answer(M7)
                        if number2==8:
                            await message.answer(M8)
                        if number2==9:
                            await message.answer(M9)
                        if number2==10:
                            await message.answer(M10)
                        if number2==11:
                            await message.answer(M11)
                    else:
                        await message.answer(f"Задания с таким номером не существует :(")


        elif text in ["Информатика"]:
            async with state.proxy() as data3:
                data3['type'] = message.text
                await Rules.request.set()
                await message.answer(text="Укажите номер задания с 1 по 27", reply_markup=types.ReplyKeyboardRemove())
            @dp.message_handler(state=Rules.request)
            async def rules2v3(message: types.Message, state: FSMContext) -> None:
                await Rules.request.set()
                async with state.proxy() as data3:
                    data3['request'] = message.text
                    number3 = int(data3['request'])
                    await state.finish()
                    if 3<=number3<=27:
                        if number3==1:
                            await message.answer("У данного номера нету программного решения")
                        if number3==2:
                            await message.answer(I2)
                        if number3==3:
                            await message.answer("У данного номера нету программного решения")
                        if number3==4:
                            await message.answer("У данного номера нету программного решения")
                        if number3==5:
                            await message.answer(I5)
                        if number3==6:
                            await message.answer(I6)
                        if number3==7:
                            await message.answer("У данного номера нету программного решения")
                        if number3==8:
                            await message.answer(I8)
                        if number3==9:
                            await message.answer("У данного номера нету программного решения")
                        if number3==10:
                            await message.answer("У данного номера нету программного решения")
                        if number3==11:
                            await message.answer("У данного номера нету программного решения")
                        if number3==12:
                            await message.answer(I12)
                        if number3==13:
                            await message.answer("У данного номера нету программного решения")
                        if number3==14:
                            await message.answer(I14)
                        if number3==15:
                            await message.answer(I15)
                        if number3==16:
                            await message.answer(I16)
                        if number3==17:
                            await message.answer(I17)
                        if number3==18:
                            await message.answer("У данного номера нету программного решения")
                        if number3==19:
                            await message.answer(I19)
                        if number3==20:
                            await message.answer(I20)
                        if number3==21:
                            await message.answer(I21)
                        if number3==22:
                            await message.answer("У данного номера нету программного решения")
                        if number3==23:
                            await message.answer(I23)
                        if number3==24:
                            await message.answer(I24)
                        if number3==25:
                            await message.answer(I25)
                        if number3==26:
                            await message.answer("У данного номера нету программного решения")
                        if number3==27:
                            await message.answer("У данного номера нету программного решения")

                    else:
                        await message.answer(f"Задания с таким номером не существует :(")

#########################################################################################################################


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
