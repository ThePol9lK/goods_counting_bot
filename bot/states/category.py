from telebot.handler_backends import State, StatesGroup


class AddCategoryState(StatesGroup):
    """Класс с состояниями бота"""

    name = State()

class DeleteCategoryState(StatesGroup):
    """Класс с состояниями бота"""

    choice = State()

class UpdateCategoryState(StatesGroup):
    """Класс с состояниями бота"""

    choice = State()
    name = State()
