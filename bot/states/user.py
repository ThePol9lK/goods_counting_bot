from telebot.handler_backends import State, StatesGroup


class UserState(StatesGroup):
    """Класс с состояниями бота"""

    name = State()
    telegram = State()
    admin = State()
