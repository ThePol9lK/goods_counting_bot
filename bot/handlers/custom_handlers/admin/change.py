import requests

from telebot.types import CallbackQuery, Message
from loader import bot

from states.user import DeleteUserState
from states.product import DeleteProductState
from states.category import UpdateCategoryState


@bot.callback_query_handler(func=lambda call: True, state=UpdateCategoryState.choice)
def choice_category(call: CallbackQuery):
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as add_data:
        add_data['id_category'] = int(call.data)
    bot.send_message(call.from_user.id, "Напиши новое название")
    bot.set_state(call.from_user.id, UpdateCategoryState.name, call.message.chat.id)


@bot.message_handler(state=UpdateCategoryState.name)
def update_name_category(message: Message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as add_data:
        url = f"http://10.5.0.5:8000/category/{add_data['id_category']}"
        param = {'name': message.text}
        print(url, param)
        queryResponse = requests.put(url, json=param)
        if queryResponse.status_code == 200:
            bot.send_message(message.from_user.id, "Категория изменена")
        else:
            bot.send_message(message.from_user.id, "Произошла ошибка")
    bot.delete_state(message.from_user.id, message.chat.id)
