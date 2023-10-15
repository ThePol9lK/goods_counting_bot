import base64
import os

import requests
from telebot.types import Message, CallbackQuery

from loader import bot

from keyboards.inline.admin_kb import template_kb, action_kb

from states.admin import AdminState

from states.user import AddUserState, DeleteUserState, UpdateUserState
from states.product import AddProductState, DeleteProductState, UpdateProductState
from states.category import AddCategoryState, DeleteCategoryState, UpdateCategoryState

from keyboards.inline.category_kb import get_category_kb, get_user_kb, get_product_kb


@bot.message_handler(commands=["admin"])
def select_template(message: Message):
    bot.send_message(message.from_user.id, "Выбери категорию из меню", reply_markup=template_kb())
    bot.set_state(message.from_user.id, AdminState.step_1, message.chat.id)

# ##
# @bot.message_handler(commands=["select"])
# def select_template(message: Message):
#     url = 'http://10.5.0.5:8000/product/3'
#     queryResponse = requests.get(url).json()
#     img = base64.b64decode(queryResponse['image'])
#     text = queryResponse['description']
#     bot.send_photo(message.from_user.id, img, caption=text)
# ##

@bot.callback_query_handler(func=lambda call: True, state=AdminState.step_1)
def select_action(call: CallbackQuery):
    bot.set_state(call.from_user.id, AdminState.step_2, call.message.chat.id)
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        data['template'] = call.data

    bot.send_message(call.from_user.id, "Выбери значение из меню", reply_markup=action_kb())


@bot.callback_query_handler(func=lambda call: call.data == 'add', state=AdminState.step_2)
def check_action(call: CallbackQuery):
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        if data['template'] == 'user':
            bot.set_state(call.from_user.id, AddUserState.name, call.message.chat.id)
            bot.send_message(call.from_user.id, "Напиши имя и фамилию нового пользователя")
        elif data['template'] == 'category':
            bot.set_state(call.from_user.id, AddCategoryState.name, call.message.chat.id)
            bot.send_message(call.from_user.id, "Напиши имя категории")
        elif data['template'] == 'product':
            bot.set_state(call.from_user.id, AddProductState.name, call.message.chat.id)
            bot.send_message(call.from_user.id, "Напиши имя товара")


@bot.callback_query_handler(func=lambda call: call.data == 'delete', state=AdminState.step_2)
def check_action(call: CallbackQuery):
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        if data['template'] == 'user':
            bot.set_state(call.from_user.id, DeleteUserState.choice, call.message.chat.id)
            bot.send_message(call.from_user.id, "Выбери пользователя для удаления", reply_markup=get_user_kb())
        elif data['template'] == 'category':
            bot.set_state(call.from_user.id, DeleteCategoryState.choice, call.message.chat.id)
            bot.send_message(call.from_user.id, "Выбери категорию для удаления", reply_markup=get_category_kb())
        elif data['template'] == 'product':
            bot.set_state(call.from_user.id, DeleteProductState.choice, call.message.chat.id)
            bot.send_message(call.from_user.id, "Выбери товар для удаления", reply_markup=get_product_kb())


@bot.callback_query_handler(func=lambda call: call.data == 'change', state=AdminState.step_2)
def check_action(call: CallbackQuery):
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        if data['template'] == 'user':
            bot.set_state(call.from_user.id, UpdateUserState.choice, call.message.chat.id)
            bot.send_message(call.from_user.id, "Выбери пользователя для изменения", reply_markup=get_user_kb())
        elif data['template'] == 'category':
            bot.set_state(call.from_user.id, UpdateCategoryState.choice, call.message.chat.id)
            bot.send_message(call.from_user.id, "Выбери категорию для изменения", reply_markup=get_category_kb())
        elif data['template'] == 'product':
            bot.set_state(call.from_user.id, UpdateProductState.choice, call.message.chat.id)
            bot.send_message(call.from_user.id, "Выбери товар для изменения", reply_markup=get_product_kb())

