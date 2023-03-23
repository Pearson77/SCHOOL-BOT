from aiogram.dispatcher.filters.state import StatesGroup, State
from cfg import ACCESS


class Answers(StatesGroup):
    """Класс именно для ответов"""
    subject = State()
    type = State()
    request = State()


class Rules(StatesGroup):
    """Класс для поиска правил"""
    subject = State()
    type = State()
    request = State()


def access_try(user_id: int) -> int:
    """На будущее, когда необходимо будет контролировать доступ к боту"""
    return 1 if user_id in ACCESS else 0
