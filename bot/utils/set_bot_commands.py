"""
Выводит базовые команды в меню
"""

from telebot.types import BotCommand
from config_data.config import DEFAULT_COMMANDS, CUSTOM_COMMANDS
from logs.loggers import func_logger
from telebot import TeleBot

@func_logger
def set_bot_commands(bot: TeleBot):
    """
    Вывод всех команд
    :param bot: Telebot
    :return:
    """
    bot.set_my_commands(
        (BotCommand(*i) for i in CUSTOM_COMMANDS + DEFAULT_COMMANDS)
    )
