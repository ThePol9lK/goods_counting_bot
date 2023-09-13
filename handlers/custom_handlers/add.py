from telebot.types import Message, CallbackQuery

from database.database import set_category, set_good
from keyboards.inline.category_kb import choise_category
from loader import bot
from logs.loggers import func_logger
from states.add_good import AddGoods


@bot.message_handler(commands=["add"])
@func_logger
def add_good(message: Message):
    bot.set_state(message.from_user.id, AddGoods.category)
    bot.send_message(message.from_user.id, 'Выбери категорию товара или введи ее название', reply_markup=choise_category())
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['chat_id'] = message.from_user.id

@bot.message_handler(state=AddGoods.category, func=lambda message: True, content_types=['text'])
@func_logger
def add_category(message: Message):
    bot.set_state(message.from_user.id, AddGoods.write_good)
    bot.send_message(message.from_user.id, 'Добавил новую категорию')
    set_category(message.text)
    bot.send_message(message.from_user.id, 'Напиши товар и его количество через пробел')
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['good_category'] = message.text


@bot.callback_query_handler(func=None, state=AddGoods.category)
@func_logger
def choice_category(call: CallbackQuery):
    bot.set_state(call.from_user.id, AddGoods.write_good)
    bot.send_message(call.from_user.id, 'Выбрали категорию')
    bot.send_message(call.from_user.id, 'Напиши товар и его количество через пробел')
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        cat_id: str = call.data
        data['good_category'] = cat_id


@bot.message_handler(state=AddGoods.write_good)
@func_logger
def choice_category(message: Message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        good_list = message.text.split()
        data['name_good'] = good_list[0]
        data['count_good'] = good_list[1]
    set_good(data)
    bot.delete_state(message.from_user.id, message.chat.id)
    bot.send_message(message.from_user.id, 'Ваш товар успешно добавлен')
