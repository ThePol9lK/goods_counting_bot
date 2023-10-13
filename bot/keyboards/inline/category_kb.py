import requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_category_kb() -> InlineKeyboardMarkup:
    """
    Клавиатура для inline кнопок
    :param:
    :return: keyboard: InlineKeyboardMarkup
    """
    url = 'http://10.5.0.5:8000/category/all'
    queryResponse = requests.get(url).json()

    return InlineKeyboardMarkup(
        keyboard=[
            [
                InlineKeyboardButton(
                    text=cat['name'],
                    callback_data=cat['id']
                )
            ] for cat in queryResponse
        ]
    )
