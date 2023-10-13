import requests
from telebot.types import Message, CallbackQuery


from loader import bot



@bot.message_handler(commands=["check"])
def select_category(message: Message):
    bot.send_message(message.from_user.id, str(requests.get('http://10.5.0.5:8000/user/2')))
