from telebot.handler_backends import State, StatesGroup


class AddGoods(StatesGroup):
    """Класс с состояниями бота"""

    category = State()
    write_good = State()
