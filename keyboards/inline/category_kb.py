from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from database.database import get_category


def choise_category() -> InlineKeyboardMarkup:
    """
    Клавиатура для inline кнопок
    :param:
    :return: keyboard: InlineKeyboardMarkup
    """
    return InlineKeyboardMarkup(
        keyboard=[
            [
                InlineKeyboardButton(
                    text=cat.name_category,
                    callback_data=cat.id_category
                )
            ] for cat in get_category()
        ]
    )
