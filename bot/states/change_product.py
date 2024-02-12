from telebot.handler_backends import State, StatesGroup


class ChangeProduct(StatesGroup):
    """Класс с состояниями бота"""
    id_category = State()
    name = State()
    count = State()
    description = State()
    finish = State()
