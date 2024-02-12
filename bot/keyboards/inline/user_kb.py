from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def user_kb() -> InlineKeyboardMarkup:
    """
    Клавиатура выбора шаблонов
    :param:
    :return: keyboard: InlineKeyboardMarkup
    """
    template_dict = {
        "Взять товар": "get",
        "Назад": "back"
    }

    return InlineKeyboardMarkup(
        keyboard=[
            [
                InlineKeyboardButton(
                    text=button,
                    callback_data=template_dict[button]
                )
            ] for button in template_dict
        ]
    )
