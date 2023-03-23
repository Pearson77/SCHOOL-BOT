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


def is_answers(search_type: str, subject: str, number: int) -> int:
    """Проверка на адекватность запроса: 1 — корректный, 0 — некорректный"""
    if search_type == "По варианту":
        if (subject == "Информатика" and number <= 20) or (subject == "Русский язык" and number <= 50):
            return 1
    elif search_type == "По заданию":
        if number <= 27:
            return 1
    return 0
    # 0 здесь вернется в том случае, если не отработает ни один вышестоящий return
