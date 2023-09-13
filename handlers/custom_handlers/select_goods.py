from telebot.types import Message

from database.database import get_goods
from loader import bot
from logs.loggers import func_logger


@bot.message_handler(commands=["select"])
def add_good(message: Message):
    goods = get_goods()
    goods_str = ''
    print(goods)
    for good in goods:
        goods_str += f'Имя товара: {good.name_good} - Количество: {good.count_good}\n'

    bot.send_message(message.from_user.id, f'Вот ваш список товаров:\n{goods_str}')
