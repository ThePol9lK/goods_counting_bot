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

def get_user_kb() -> InlineKeyboardMarkup:
    """
    Клавиатура для inline кнопок
    :param:
    :return: keyboard: InlineKeyboardMarkup
    """
    url = 'http://10.5.0.5:8000/user/all'
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

def get_product_kb(cat_id) -> InlineKeyboardMarkup:
    """
    Клавиатура для inline кнопок
    :param:
    :return: keyboard: InlineKeyboardMarkup
    """
    url = f'http://10.5.0.5:8000/product/all/{cat_id}'
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
