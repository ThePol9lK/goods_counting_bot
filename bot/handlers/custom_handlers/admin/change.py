import base64

import requests

from telebot.types import CallbackQuery, Message
from loader import bot

from states.user import UpdateUserState
from states.product import UpdateProductState
from states.category import UpdateCategoryState

from keyboards.inline.admin_kb import is_admin_kb
from keyboards.inline.category_kb import get_product_kb



# Изменение пользователя
@bot.callback_query_handler(func=lambda call: True, state=UpdateUserState.choice)
def choice_user(call: CallbackQuery):
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as add_data:
        add_data['id_user'] = int(call.data)
    bot.send_message(call.from_user.id, "Напиши новое название")
    bot.set_state(call.from_user.id, UpdateUserState.name, call.message.chat.id)


@bot.message_handler(state=UpdateUserState.name)
def update_name_user(message: Message):
    bot.send_message(message.from_user.id, "Напиши id telegram")
    bot.set_state(message.from_user.id, UpdateUserState.telegram, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as add_data:
        add_data['name'] = message.text


@bot.message_handler(state=UpdateUserState.telegram)
def update_telegram(message: Message):
    bot.send_message(message.from_user.id, "Будет он администратором", reply_markup=is_admin_kb())
    bot.set_state(message.from_user.id, UpdateUserState.telegram, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as add_data:
        add_data['id_telegram'] = message.text


@bot.callback_query_handler(func=lambda call: True, state=UpdateUserState.telegram)
def update_admin(call: CallbackQuery):
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as add_data:
        add_data['admin'] = call.data
        bot.send_message(call.from_user.id,
                         f"Проверка данных: Имя нового пользователя - {add_data['name']}, Значение id_telegram {add_data['id_telegram']} {add_data['admin']}",
                         reply_markup=is_admin_kb())
    bot.set_state(call.from_user.id, UpdateUserState.admin, call.message.chat.id)


@bot.callback_query_handler(func=lambda call: True, state=UpdateUserState.admin)
def update_user(call: CallbackQuery):
    if call.data == 'True':
        with bot.retrieve_data(call.from_user.id, call.message.chat.id) as add_data:
            url = f"http://10.5.0.5:8000/user/{add_data['id_user']}"
            param = {'name': add_data['name'], 'id_telegram': add_data['id_telegram'], 'admin': bool(add_data['admin'])}
            queryResponse = requests.put(url, json=param)
            if queryResponse.status_code == 200:
                bot.send_message(call.from_user.id, "Новый пользователь добавлен")
            else:
                bot.send_message(call.from_user.id, "Произошла ошибка")
    else:
        bot.send_message(call.from_user.id, "Не будем добавлять пользователя")
    bot.delete_state(call.from_user.id, call.message.chat.id)


# Изменение категории
@bot.callback_query_handler(func=lambda call: True, state=UpdateCategoryState.choice)
def choice_category(call: CallbackQuery):
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as add_data:
        add_data['id_category'] = int(call.data)
    bot.send_message(call.from_user.id, "Напиши новое название")
    bot.set_state(call.from_user.id, UpdateCategoryState.name, call.message.chat.id)


@bot.message_handler(state=UpdateCategoryState.name)
def update_name_category(message: Message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as add_data:
        url = f"http://10.5.0.5:8000/category/{add_data['id_user']}"
        param = {'name': message.text}
        print(url, param)
        queryResponse = requests.put(url, json=param)
        if queryResponse.status_code == 200:
            bot.send_message(message.from_user.id, "Категория изменена")
        else:
            bot.send_message(message.from_user.id, "Произошла ошибка")
    bot.delete_state(message.from_user.id, message.chat.id)


# Изменение товара

@bot.callback_query_handler(func=lambda call: True, state=UpdateProductState.id_category)
def choice_user(call: CallbackQuery):
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as add_data:
        add_data['id_category'] = int(call.data)
        bot.send_message(call.from_user.id, "Напиши новое название", reply_markup=get_product_kb(int(call.data)))
    bot.set_state(call.from_user.id, UpdateProductState.choice, call.message.chat.id)


@bot.callback_query_handler(func=lambda call: True, state=UpdateProductState.choice)
def choice_user(call: CallbackQuery):
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as add_data:
        add_data['id_product'] = int(call.data)
    bot.send_message(call.from_user.id, "Напиши новое название")
    bot.set_state(call.from_user.id, UpdateProductState.name, call.message.chat.id)


@bot.message_handler(state=UpdateProductState.name)
def add_name_product(message: Message):
    bot.send_message(message.from_user.id, "Напиши количество продукта")
    bot.set_state(message.from_user.id, UpdateProductState.count, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as add_data:
        add_data['name'] = message.text


@bot.message_handler(state=UpdateProductState.count)
def add_count_product(message: Message):
    bot.send_message(message.from_user.id, "Напиши описание продукта")
    bot.set_state(message.from_user.id, UpdateProductState.description, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as add_data:
        add_data['count'] = int(message.text)


@bot.message_handler(state=UpdateProductState.description)
def add_description_product(message: Message):
    bot.send_message(message.from_user.id, "Пришли фото продукта")
    bot.set_state(message.from_user.id, UpdateProductState.image, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as add_data:
        add_data['description'] = message.text


@bot.message_handler(state=UpdateProductState.image, content_types=['photo'])
def add_photo_product(message: Message):
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as add_data:
        url = f"http://10.5.0.5:8000/product/{add_data['id_product']}"
        param = {'name': add_data['name'],
                 'count': add_data['count'],
                 'description': add_data['description'],
                 'image': base64.encodebytes(downloaded_file).decode('utf-8'),
                 'id_category': add_data['id_category']}
        queryResponse = requests.put(url, json=param)
        if queryResponse.status_code == 200:
            bot.send_message(message.from_user.id, "Товар измене")
        else:
            bot.send_message(message.from_user.id, "Произошла ошибка")
    bot.delete_state(message.from_user.id, message.chat.id)
