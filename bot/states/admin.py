from telebot.handler_backends import State, StatesGroup


class AdminState(StatesGroup):
    """Класс с состояниями бота"""

    template = State()
    name = State()
    telegram = State()
    admin = State()

