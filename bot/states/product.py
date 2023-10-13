from telebot.handler_backends import State, StatesGroup


class ProductState(StatesGroup):
    """Класс с состояниями бота"""

    name = State()
    count = State()
    description = State()
    image = State()
    id_category = State()
