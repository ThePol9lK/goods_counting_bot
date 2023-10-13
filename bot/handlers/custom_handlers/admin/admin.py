import os

import requests
from telebot.types import Message, CallbackQuery

from loader import bot

from keyboards.inline.admin_kb import template_kb, action_kb

from states.admin import AdminState

from states.user import UserState
from states.product import ProductState
from states.category import CategoryState

from keyboards.inline.category_kb import get_category_kb


@bot.message_handler(commands=["admin"])
def select_template(message: Message):
    bot.send_message(message.from_user.id, "Выбери категорию из меню", reply_markup=template_kb())
    bot.set_state(message.from_user.id, AdminState.template, message.chat.id)


@bot.callback_query_handler(func=lambda call: True, state=AdminState.template)
def select_action(call: CallbackQuery):
    bot.set_state(call.from_user.id, UserState.name, call.message.chat.id)
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        data['template'] = call.data

    bot.send_message(call.from_user.id, "Выбери значение из меню", reply_markup=action_kb())


@bot.callback_query_handler(func=lambda call: call.data == 'add', state=UserState.name)
def check_action(call: CallbackQuery):
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        if data['template'] == 'user':
            bot.set_state(call.from_user.id, UserState.name, call.message.chat.id)
            bot.send_message(call.from_user.id, "Напиши имя и фамилию нового пользователя")
        elif data['template'] == 'category':
            bot.set_state(call.from_user.id, CategoryState.name, call.message.chat.id)
            bot.send_message(call.from_user.id, "Напиши имя категории")
        elif data['template'] == 'product':
            bot.set_state(call.from_user.id, ProductState.name, call.message.chat.id)
            bot.send_message(call.from_user.id, "Напиши имя товара")


@bot.callback_query_handler(func=lambda call: call.data == 'delete', state=UserState.name)
def check_action(call: CallbackQuery):
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        if data['template'] == 'user':
            bot.send_message(call.from_user.id, "Удалить пользователя")
        elif data['template'] == 'category':
            bot.send_message(call.from_user.id, "Удалить категорию")
        elif data['template'] == 'product':
            bot.send_message(call.from_user.id, "Удалить товар")


@bot.callback_query_handler(func=lambda call: call.data == 'change', state=UserState.name)
def check_action(call: CallbackQuery):
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        if data['template'] == 'user':
            bot.send_message(call.from_user.id, "Изменение пользователя")
        elif data['template'] == 'category':
            bot.send_message(call.from_user.id, "Изменение категории")
        elif data['template'] == 'product':
            bot.send_message(call.from_user.id, "Изменение товара")
