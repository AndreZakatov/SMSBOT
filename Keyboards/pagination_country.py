from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from SMS_HUB.misc.list_country import countries

def create_pagination_keyboard(page: int, items_per_page: int = 10) -> InlineKeyboardMarkup:
    start_index = page * items_per_page
    end_index = start_index + items_per_page
    page_countries = list(countries.keys())[start_index:end_index]

    kb_builder = InlineKeyboardBuilder()

    # Добавляем в билдер ряд с кнопками
    for button in page_countries:
        kb_builder.row(InlineKeyboardButton(
            text=countries[button],
            callback_data=f"country_{button}")
        )

    # Добавляем кнопки для навигации по страницам
    prev_button = InlineKeyboardButton(text="<< Назад", callback_data=f"prev_page_{page}")
    next_button = InlineKeyboardButton(text="Вперед >>", callback_data=f"next_page_{page}")
    kb_builder.row(prev_button, next_button)

    return kb_builder.as_markup()

