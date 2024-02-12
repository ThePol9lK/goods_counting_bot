# import requests
#
# from loader import bot
# from telebot.types import CallbackQuery, Message
#
# from datetime import datetime
#
# import openpyxl
#
# from openpyxl.worksheet import worksheet
# from openpyxl.styles import Font, Fill, PatternFill, NamedStyle, Side, Border
#
#
# @bot.message_handler(commands=["excel"])
# def create_excel(message: Message):
#     book = openpyxl.Workbook()
#     book.remove(book.active)
#
#     sheet_1 = book.create_sheet("Склад")
#
#     sheet: worksheet = book.worksheets[0]
#
#     #Начало ексель файла
#     font = Font(b=True, size=14, color="000000")
#     sheet['A2'].font = font
#     sheet["A2"].value = "Ведомость по товарам на складах"
#
#     sheet["A4"].value = "Параметры:"
#     sheet["B4"].value = f"Период:{datetime.now().date()}"
#
#     sheet["A6"].value = "Склад"
#     sheet["D6"].value = "Количество"
#
#     sheet["A7"].value = 'Артикул'
#     sheet["B7"].value = 'Номенклатура, Характеристика'
#     sheet["C7"].value = 'Ед. изм.'
#
#     sheet["D7"].value = 'Начальный остаток'
#     sheet["E7"].value = 'Приход'
#     sheet["F7"].value = 'Расход'
#     sheet["G7"].value = 'Конечный остаток'
#
#     url = 'http://10.5.0.5:8000/user/all'
#     queryResponse = requests.get(url).json()
#     for i in range(len(queryResponse)):
#
#     A =         [
#                 InlineKeyboardButton(
#                     text=cat['name'],
#                     callback_data=cat['id']
#                 )
#             ] for cat in queryResponse
#
#
#
#
#     A = ['Адаптер, TP-LINK POE 24V  - Адаптер',
#          'Адаптер, USB to Ethernet  - Адаптер',
#          'Адаптер, Инжектор PoE  - Адаптер']
#
#     B = [12,
#          1,
#          22]
#
#     # Запись данных ексель файла
#     for i in range(len(A)):
#         sheet.cell(row=8 + i, column=2).value = A[i]
#
#     for i in range(len(B)):
#         sheet.cell(row=8 + i, column=7).value = B[i]
#
#     sheet.cell(row=8 + len(A), column=1).value = 'Итого'
#     sheet.cell(row=8 + len(A), column=7).value = f'=SUM(G8:G{8 + len(A) - 1})'
#
#     book.save("..\\excel\\test.xlsx")
