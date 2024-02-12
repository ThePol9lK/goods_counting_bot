import base64

import requests
from loader import bot
from telebot.types import CallbackQuery, Message

from states.change_product import ChangeProduct

from keyboards.inline.category_kb import get_category_kb
from keyboards.inline.category_kb import get_product_kb

from keyboards.inline.user_kb import user_kb


@bot.message_handler(commands=["change"])
def get_category(message: Message):
    bot.send_message(message.from_user.id, "Выбери категорию товара для изменения", reply_markup=get_category_kb())
    bot.set_state(message.from_user.id, ChangeProduct.id_category, message.chat.id)


@bot.callback_query_handler(func=lambda call: True, state=ChangeProduct.id_category)
def get_product(call: CallbackQuery):
    bot.send_message(call.from_user.id, "Напиши новое название", reply_markup=get_product_kb(int(call.data)))
    bot.set_state(call.from_user.id, ChangeProduct.name, call.message.chat.id)


@bot.callback_query_handler(func=lambda call: True, state=ChangeProduct.name)
def show_product(call: CallbackQuery):
    url = f'http://10.5.0.5:8000/product/{int(call.data)}'
    queryResponse = requests.get(url).json()
    img = base64.b64decode(queryResponse['image'])
    text = f"Имя товара - {queryResponse['name']}\nОписание товара - {queryResponse['description']}\nКоличество " \
           f"товара - {queryResponse['count']} "
    bot.send_photo(call.from_user.id, img, caption=text, reply_markup=user_kb())
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as add_data:
        add_data['id_category'] = int(call.data)
    bot.set_state(call.from_user.id, ChangeProduct.count, call.message.chat.id)


@bot.callback_query_handler(func=lambda call: True, state=ChangeProduct.count)
def count_transaction(call: CallbackQuery):
    if call.data == 'get':
        bot.send_message(call.from_user.id, "Сколько товара тебе надо забрать?")
        bot.set_state(call.from_user.id, ChangeProduct.description, call.message.chat.id)
    elif call.data == 'back':
        bot.send_message(call.from_user.id, "Напиши еще раз команду /change")
        bot.delete_state(call.from_user.id, call.message.chat.id)


@bot.message_handler(state=ChangeProduct.description)
def description_transaction(message: Message):
    bot.send_message(message.from_user.id, "Для чего нужно забрать товар?")
    with bot.retrieve_data(message.from_user.id, message.chat.id) as add_data:
        add_data['count'] = int(message.text)
    bot.set_state(message.from_user.id, ChangeProduct.finish, message.chat.id)


@bot.message_handler(state=ChangeProduct.finish)
def finish_transaction(message: Message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as add_data:
        url = f"http://10.5.0.5:8000/product/{add_data['id_category']}"
        queryResponse = requests.get(url).json()
        queryResponse['count'] = queryResponse['count'] - add_data['count']
        requests.put(url, json=queryResponse)

        user_url = f"http://10.5.0.5:8000/user/all"
        queryResponse_user = requests.get(user_url).json()
        for count in range(len(queryResponse_user)):
            if queryResponse_user[count]["id_telegram"] == str(message.from_user.id):
                id_user = queryResponse_user[count]["id"]

                url_transaction = 'http://10.5.0.5:8000/transaction'
                param_transaction = {
                                      "id_user": id_user,
                                      "id_product": add_data['id_category'],
                                      "description": message.text,
                                      "count": add_data['count']
                                    }
                queryResponse = requests.post(url_transaction, json=param_transaction)
                if queryResponse.status_code == 200:
                    bot.send_message(message.from_user.id, "Записали данные")
                else:
                    bot.send_message(message.from_user.id, "Произошла ошибка")
    bot.delete_state(message.from_user.id, message.chat.id)
