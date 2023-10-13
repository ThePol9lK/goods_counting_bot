from telebot.handler_backends import State, StatesGroup


class CategoryState(StatesGroup):
    """Класс с состояниями бота"""

    name = State()

