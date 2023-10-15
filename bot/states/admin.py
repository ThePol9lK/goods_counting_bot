from telebot.handler_backends import State, StatesGroup


class AdminState(StatesGroup):
    """Класс с состояниями бота"""

    step_1 = State()
    step_2 = State()

