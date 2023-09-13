import os

from peewee import SqliteDatabase, Model, CharField, IntegerField, \
    ForeignKeyField, AutoField

db = SqliteDatabase(os.path.join('database', 'bot_data.db'))


class BaseModel(Model):
    """"Класс базовой модели для ORM"""

    class Meta:
        database: SqliteDatabase = db


class User(BaseModel):
    """
    Класс Пользователь (для ORM)

    Attributes:
          id_user - id пользователя
          name - имя пользователя
          user_id - id пользователя телеграмм
          chat_id - id чата

    """
    id_user = AutoField()
    name = CharField()
    user_id = IntegerField(unique=True)
    chat_id = IntegerField()


class Category(BaseModel):
    """
    Класс Категрии (для ORM)

    Attributes:
        id_category - id категории
        name_category - наименование категории
    """
    id_category = AutoField()
    name_category = CharField()


class Good(BaseModel):
    """
    Класс Товар (для ORM)

    Attributes:
        id_good - id товара
        name_good - наименование товара
        count_good - iколичество товара на складе
        user - ключ для таблицы пользователя
        good_category - ключ для таблицы категории
    """
    id_good = AutoField()
    name_good = CharField()
    count_good = IntegerField()
    user = ForeignKeyField(User)
    good_category = ForeignKeyField(Category)
