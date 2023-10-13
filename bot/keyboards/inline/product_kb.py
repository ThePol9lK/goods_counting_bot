# from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
#
# from database.database import get_products
#
#
# def get_product_kb(category_id: int) -> InlineKeyboardMarkup:
#     """
#     Клавиатура для inline кнопок
#     :type category_id: int
#     :param:
#     :return: keyboard: InlineKeyboardMarkup
#     """
#     return InlineKeyboardMarkup(
#         keyboard=[
#             [
#                 InlineKeyboardButton(
#                     text=pr.name_product,
#                     callback_data=pr.id
#                 )
#             ] for pr in get_products(id_category=category_id)
#         ]
#     )
