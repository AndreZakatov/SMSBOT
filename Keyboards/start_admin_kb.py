from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

b_statistika = KeyboardButton(text='📊 Статистика')
b_mailing = KeyboardButton(text='📤 Рассылка')
b_setting_up_the_margin = KeyboardButton(text='💵 Настройка наценки')
b_advertising_buttons = KeyboardButton(text='⌨ Рекламные кнопки')
b_search_user = KeyboardButton(text='🔍 Поиск пользователя')
b_create_promo = KeyboardButton(text='🎁 Создание промокода')

kb_start_admin = ReplyKeyboardMarkup(keyboard=[[b_statistika, b_mailing],
                                               [b_setting_up_the_margin, b_advertising_buttons],
                                               [b_search_user, b_create_promo]], resize_keyboard=True, one_time_keyboard=True)

