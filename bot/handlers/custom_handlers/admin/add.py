import base64
import requests

from telebot.types import Message, CallbackQuery
from loader import bot

from keyboards.inline.admin_kb import is_admin_kb
from keyboards.inline.category_kb import get_category_kb

from states.user import AddUserState
from states.product import AddProductState
from states.category import AddCategoryState


# Добавление пользователя


@bot.message_handler(state=AddUserState.name)
def add_name_user(message: Message):
    bot.send_message(message.from_user.id, "Напиши id telegram")
    bot.set_state(message.from_user.id, AddUserState.telegram, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as add_data:
        add_data['name'] = message.text


@bot.message_handler(state=AddUserState.telegram)
def add_telegram(message: Message):
    bot.send_message(message.from_user.id, "Будет он администратором", reply_markup=is_admin_kb())
    bot.set_state(message.from_user.id, AddUserState.telegram, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as add_data:
        add_data['id_telegram'] = message.text


@bot.callback_query_handler(func=lambda call: True, state=AddUserState.telegram)
def add_admin(call: CallbackQuery):
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as add_data:
        add_data['admin'] = call.data
        bot.send_message(call.from_user.id,
                         f"Проверка данных: Имя нового пользователя - {add_data['name']}, Значение id_telegram {add_data['id_telegram']} {add_data['admin']}",
                         reply_markup=is_admin_kb())
    bot.set_state(call.from_user.id, AddUserState.admin, call.message.chat.id)


@bot.callback_query_handler(func=lambda call: True, state=AddUserState.admin)
def add_user(call: CallbackQuery):
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
    bot.delete_state(call.from_user.id, call.message.chat.id)


# Добавление категории

@bot.message_handler(state=AddCategoryState.name)
def add_name_category(message: Message):
    bot.delete_state(message.from_user.id, message.chat.id)
    url = 'http://10.5.0.5:8000/category'
    param = {'name': message.text}
    queryResponse = requests.post(url, json=param)
    if queryResponse.status_code == 200:
        bot.send_message(message.from_user.id, "Новая категория добавлена")
    else:
        bot.send_message(message.from_user.id, "Произошла ошибка")


# Добавление товара
@bot.message_handler(state=AddProductState.name)
def add_name_product(message: Message):
    bot.send_message(message.from_user.id, "Напиши количество продукта")
    bot.set_state(message.from_user.id, AddProductState.count, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as add_data:
        add_data['name'] = message.text


@bot.message_handler(state=AddProductState.count)
def add_count_product(message: Message):
    bot.send_message(message.from_user.id, "Напиши описание продукта")
    bot.set_state(message.from_user.id, AddProductState.description, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as add_data:
        add_data['count'] = int(message.text)


@bot.message_handler(state=AddProductState.description)
def add_description_product(message: Message):
    bot.send_message(message.from_user.id, "Выбери категорию для товара", reply_markup=get_category_kb())
    bot.set_state(message.from_user.id, AddProductState.id_category, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as add_data:
        add_data['description'] = message.text


@bot.callback_query_handler(func=lambda call: True, state=AddProductState.id_category)
def add_id_category_product(call: CallbackQuery):
    bot.send_message(call.from_user.id, "Пришли фото продукта")
    bot.set_state(call.from_user.id, AddProductState.image, call.message.chat.id)
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as add_data:
        add_data['id_category'] = call.data


@bot.message_handler(state=AddProductState.image, content_types=['photo'])
def add_photo_product(message: Message):
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as add_data:
        url = 'http://10.5.0.5:8000/product'
        param = {'name': add_data['name'],
                 'count': add_data['count'],
                 'description': add_data['description'],
                 'image': base64.encodebytes(downloaded_file).decode('utf-8'),
                 'id_category': add_data['id_category']}

        queryResponse = requests.post(url, json=param)
        if queryResponse.status_code == 200:
            bot.send_message(message.from_user.id, "Новый товар добавлен")
        else:
            bot.send_message(message.from_user.id, "Произошла ошибка")
