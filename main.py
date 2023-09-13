import os
from loguru import logger

from database.database import create_tables
from loader import bot
import handlers  # noqa
from utils.set_bot_commands import set_bot_commands
from telebot.custom_filters import StateFilter

if __name__ == "__main__":
    logger.add(os.path.join('logs', 'logs.log'),
               format='{time} {level} {message}',
               retention='2 days')
    logger.debug('#### Запущен новый сеанс ####')

    create_tables()

    bot.add_custom_filter(StateFilter(bot))
    set_bot_commands(bot)
    bot.infinity_polling()
