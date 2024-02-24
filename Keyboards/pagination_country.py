from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from SMS_HUB.misc.list_country import countries


def generate_keyboard(page):
    PAGE_SIZE = 10

    start = page * PAGE_SIZE
    end = start + PAGE_SIZE
    for country_code, country_name in list(countries.items())[start:end]:
        button = InlineKeyboardButton(text=country_name, callback_data=f"country:{country_code}")
        keyboards = InlineKeyboardMarkup(keyboards)
        keyboards.add(button)
    if start > 0:
        prev_button = InlineKeyboardButton(text="Назад", callback_data=f"prev:{page - 1}")
        keyboards.add(prev_button)
    if end < len(countries):
        next_button = InlineKeyboardButton(text="Вперед", callback_data=f"next:{page + 1}")
        keyboards.add(next_button)
    return keyboards


keyboard = generate_keyboard(page=0)

