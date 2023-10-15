from telebot.handler_backends import State, StatesGroup


class AddUserState(StatesGroup):
    """Класс с состояниями бота"""

    name = State()
    telegram = State()
    admin = State()

class DeleteUserState(StatesGroup):
    """Класс с состояниями бота"""

    choice = State()

class UpdateUserState(StatesGroup):
    """Класс с состояниями бота"""

    choice = State()
