import os
from typing import List

from peewee import SqliteDatabase

from logs.loggers import func_logger

from database.models import *

db = SqliteDatabase(os.path.join('database', 'bot_data.db'))


@func_logger
def create_tables():
    """Создает таблицы в базе данных (если они не созданы)"""

    with db:
        db.create_tables([User, Category, Good])


@func_logger
def get_category() -> List[Category]:
    """


    :param
    :return:
    """
    with db.atomic():
        query = Category.select()
    query = list(query)
    return query


@func_logger
def get_goods() -> list[Good]:
    with db.atomic():
        goods = Good.select()
    goods = list(goods)
    return goods


@func_logger
def set_user(data: dict) -> None:
    """


    :param data: словарь с данными
    """
    #if
    with db.atomic():
        User.get_or_create(
            name=data['user_name'],
            user_id=data['user_id'],
            chat_id=data['chat_id']
        )


@func_logger
def set_good(data: dict) -> None:
    """

    :param data: словарь с данными
    """
    with db.atomic():
        user = User.select().where(User.user_id == data['chat_id'])[0]
        cat = Category.select().where(Category.id_category == data['good_category'])[0]

        Good.create(
            name_good=data['name_good'],
            count_good=data['count_good'],
            user=user,
            good_category=cat
        )


@func_logger
def set_category(category: str) -> None:
    with db.atomic():
        Category.create(
            name_category=category
        )
