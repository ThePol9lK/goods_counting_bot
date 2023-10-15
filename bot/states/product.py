from telebot.handler_backends import State, StatesGroup


class AddProductState(StatesGroup):
    """Класс с состояниями бота"""

    name = State()
    count = State()
    description = State()
    image = State()
    id_category = State()

class DeleteProductState(StatesGroup):
    """Класс с состояниями бота"""

    choice = State()

class UpdateProductState(StatesGroup):
    """Класс с состояниями бота"""

    choice = State()
