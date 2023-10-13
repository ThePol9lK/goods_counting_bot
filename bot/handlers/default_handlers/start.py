from telebot.types import Message

# from database.database import set_user
from loader import bot
from logs.loggers import func_logger


@bot.message_handler(commands=["start"])
@func_logger
def bot_start(message: Message):
    # user_data = {'user_name': message.from_user.full_name, 'user_id': message.chat.id, 'chat_id': message.message_id}
    #
    # set_user(user_data)
    bot.reply_to(message, f"Привет, {message.from_user.full_name}!")
