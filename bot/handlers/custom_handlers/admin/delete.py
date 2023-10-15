import requests

from telebot.types import CallbackQuery
from loader import bot

from states.user import DeleteUserState
from states.product import DeleteProductState
from states.category import DeleteCategoryState


@bot.callback_query_handler(func=lambda call: True, state=DeleteCategoryState.choice)
def add_admin(call: CallbackQuery):
    bot.delete_state(call.from_user.id, call.message.chat.id)
    url = f'http://10.5.0.5:8000/category/{call.data}'
    queryResponse = requests.delete(url)
    if queryResponse.status_code == 200:
        bot.send_message(call.from_user.id, "Категория удалена")
    else:
        bot.send_message(call.from_user.id, "Произошла ошибка")


@bot.callback_query_handler(func=lambda call: True, state=DeleteUserState.choice)
def add_admin(call: CallbackQuery):
    bot.delete_state(call.from_user.id, call.message.chat.id)
    url = f'http://10.5.0.5:8000/user/{call.data}'
    queryResponse = requests.delete(url)
    if queryResponse.status_code == 200:
        bot.send_message(call.from_user.id, "Пользователь удален")
    else:
        bot.send_message(call.from_user.id, "Произошла ошибка")


@bot.callback_query_handler(func=lambda call: True, state=DeleteProductState.choice)
def add_admin(call: CallbackQuery):
    bot.delete_state(call.from_user.id, call.message.chat.id)
    url = f'http://10.5.0.5:8000/product/{call.data}'
    queryResponse = requests.delete(url)
    if queryResponse.status_code == 200:
        bot.send_message(call.from_user.id, "Пользователь удален")
    else:
        bot.send_message(call.from_user.id, "Произошла ошибка")
