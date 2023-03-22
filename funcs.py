from aiogram.dispatcher.filters.state import StatesGroup, State
from cfg import ACCESS


class Answers(StatesGroup):
    subject = State()
    type = State()
    request = State()


class Rules(StatesGroup):
    subject = State()
    request = State()


def access_try(user_id: int) -> int:
    """На будущее, когда необходимо будет контролировать доступ к боту"""
    return 1 if user_id in ACCESS else 0
