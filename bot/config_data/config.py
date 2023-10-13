import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку")
)

CUSTOM_COMMANDS = (
    ('add', 'Добавление товара в базу данных'),
    ('delete', 'Удаление товары из базы данных'),
    ('select', 'Список товаров'),
)

