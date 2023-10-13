# from telebot.types import Message, CallbackQuery
#
# from database.database import get_product
# from keyboards.inline.category_kb import get_category_kb
# from keyboards.inline.change_count_kb import change_count_kb
# from keyboards.inline.product_kb import get_product_kb
#
# from loader import bot
# from logs.loggers import func_logger
# from states.get_product import Get_Product
#
#
# @bot.message_handler(commands=["select"])
# def select_category(message: Message):
#     bot.set_state(message.from_user.id, Get_Product.category)
#     bot.send_message(message.from_user.id, 'Выбери категорию', reply_markup=get_category_kb())
#
#
# @bot.callback_query_handler(func=None, state=Get_Product.category)
# def select_product(call: CallbackQuery):
#     bot.set_state(call.from_user.id, Get_Product.product_get)
#     callback_data = int(call.data)
#     bot.send_message(call.from_user.id, 'Выбери товар из категории', reply_markup=get_product_kb(callback_data))
#
# @bot.callback_query_handler(func=None, state=Get_Product.product_get)
# def select_product(call: CallbackQuery):
#     bot.delete_state(call.from_user.id, call.message.chat.id)
#     callback_data = int(call.data)
#     product = get_product(callback_data)
#     product_photo = open(product[0].photo_product, 'rb')
#     product_description = f'Товар - {product[0].name_product}\n' \
#                                 f'Количество товара - {product[0].count_product}\n' \
#                                 f'Описание товара - {product[0].description_product}\n'
#     bot.send_photo(call.from_user.id, photo=product_photo, caption=product_description, reply_markup=change_count_kb())
