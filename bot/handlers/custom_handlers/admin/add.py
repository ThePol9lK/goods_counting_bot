import os
import requests

from telebot.types import Message, CallbackQuery
from loader import bot

from keyboards.inline.admin_kb import is_admin_kb
from keyboards.inline.category_kb import get_category_kb

from states.user import UserState
from states.product import ProductState
from states.category import CategoryState


# Добавление пользователя


@bot.message_handler(state=UserState.name)
def add_name_user(message: Message):
    bot.send_message(message.from_user.id, "Напиши id telegram")
    bot.set_state(message.from_user.id, UserState.telegram, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as add_data:
        add_data['name'] = message.text


@bot.message_handler(state=UserState.telegram)
def add_telegram(message: Message):
    bot.send_message(message.from_user.id, "Будет он администратором", reply_markup=is_admin_kb())
    bot.set_state(message.from_user.id, UserState.telegram, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as add_data:
        add_data['id_telegram'] = message.text


@bot.callback_query_handler(func=lambda call: True, state=UserState.telegram)
def add_admin(call: CallbackQuery):
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as add_data:
        add_data['admin'] = call.data
        bot.send_message(call.from_user.id,
                         f"Проверка данных: Имя нового пользователя - {add_data['name']}, Значение id_telegram {add_data['id_telegram']} {add_data['admin']}",
                         reply_markup=is_admin_kb())
    bot.set_state(call.from_user.id, UserState.admin, call.message.chat.id)


@bot.callback_query_handler(func=lambda call: True, state=UserState.admin)
def add_user(call: CallbackQuery):
    bot.delete_state(call.from_user.id, call.message.chat.id)
    if call.data == 'True':
        url = 'http://10.5.0.5:8000/user'
        with bot.retrieve_data(call.from_user.id, call.message.chat.id) as add_data:
            param = {'name': add_data['name'], 'id_telegram': add_data['id_telegram'], 'admin': bool(add_data['admin'])}
            queryResponse = requests.post(url, json=param)
            if queryResponse.status_code == 200:
                bot.send_message(call.from_user.id, "Новый пользователь добавлен")
            else:
                bot.send_message(call.from_user.id, "Произошла ошибка")
    else:
        bot.send_message(call.from_user.id, "Не будем добавлять пользователя")


# Добавление категории

@bot.message_handler(state=CategoryState.name)
def add_name_category(message: Message):
    bot.delete_state(message.from_user.id, message.chat.id)
    url = 'http://10.5.0.5:8000/category'
    param = {'name': message.text}
    queryResponse = requests.post(url, json=param)
    if queryResponse.status_code == 200:
        bot.send_message(message.from_user.id, "Новый пользователь добавлен")
    else:
        bot.send_message(message.from_user.id, "Произошла ошибка")


# Добавление товара
@bot.message_handler(state=ProductState.name)
def add_name_product(message: Message):
    bot.send_message(message.from_user.id, "Напиши количество продукта")
    bot.set_state(message.from_user.id, ProductState.count, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as add_data:
        add_data['name'] = message.text


@bot.message_handler(state=ProductState.count)
def add_count_product(message: Message):
    bot.send_message(message.from_user.id, "Напиши описание продукта")
    bot.set_state(message.from_user.id, ProductState.description, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as add_data:
        add_data['count'] = int(message.text)


@bot.message_handler(state=ProductState.description)
def add_description_product(message: Message):
    bot.send_message(message.from_user.id, "Пришли фото продукта")
    bot.set_state(message.from_user.id, ProductState.image, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as add_data:
        add_data['description'] = message.text


@bot.message_handler(state=ProductState.image, content_types=['photo'])
def add_photo_product(message: Message):
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    file_unique_id = file_info.file_unique_id
    file_extension = file_info.file_path.split('.')[-1]

    current_dir = os.getcwd()
    # Путь до папки, находящейся на директорию ниже
    folder_path = os.path.join(current_dir, "..", "api", "image")
    # Путь до файла
    file_path = os.path.normpath(os.path.join(folder_path, f'{file_unique_id}.{file_extension}'))

    with open(file_path, 'wb') as new_file:
        new_file.write(downloaded_file)

    bot.send_message(message.from_user.id, "Выбери категорию товаров", reply_markup=get_category_kb())
    # bot.set_state(message.from_user.id, ProductState.id_category, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as add_data:
        url = 'http://10.5.0.5:8000/product'
        param = {'name': add_data['name'], 'count': add_data['count'], 'description': add_data['description'], 'image': ..., 'id_category': 1}

        queryResponse = requests.post(url, json=param)
        if queryResponse.status_code == 200:
            bot.send_message(message.from_user.id, "Новый пользователь добавлен")
        else:
            bot.send_message(message.from_user.id, "Произошла ошибка")

        add_data['image'] = file_path
        print(add_data)


@bot.callback_query_handler(func=lambda call: True, state=ProductState.id_category)
def add_id_category_product(call: CallbackQuery):
    print(call)
    #
    # bot.delete_state(call.from_user.id, call.message.chat.id)
    # if call.data == 'True':
    #     url = 'http://10.5.0.5:8000/user'
    #     with bot.retrieve_data(call.from_user.id, call.message.chat.id) as add_data:
    #         param = {'name': add_data['name'], 'id_telegram': add_data['id_telegram'], 'admin': bool(add_data['admin'])}
    #         queryResponse = requests.post(url, json=param)
    #         if queryResponse.status_code == 200:
    #             bot.send_message(call.from_user.id, "Новый пользователь добавлен")
    #         else:
    #             bot.send_message(call.from_user.id, "Произошла ошибка")
    # else:
    #     bot.send_message(call.from_user.id, "Не будем добавлять пользователя")
