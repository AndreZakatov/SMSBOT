from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

b_balance = InlineKeyboardButton(text='🏦 Баланс',
                                 callback_data='balance')
b_buy_number = InlineKeyboardButton(text='📲 Купить',
                                    callback_data='pay')
b_replenishment = InlineKeyboardButton(text='💸 Пополнение',
                                       callback_data='replenishment')
b_rent = InlineKeyboardButton(text='⏰ Арендовать',
                              callback_data='rent')
b_multiservic = InlineKeyboardButton(text='☎️ Мультисервис',
                                     callback_data='multiservice')
b_history = InlineKeyboardButton(text='💾 История',
                                 callback_data='history')
b_promo = InlineKeyboardButton(text='🎁 Создание промокода',
                               callback_data='promo')
b_favourites = InlineKeyboardButton(text='✨ Избранное',
                                    callback_data='favourites')
b_referrals = InlineKeyboardButton(text='👥 Рефералы',
                                   callback_data='referals')
b_profile = InlineKeyboardButton(text='🎩 Профиль',
                                 callback_data='profile')

user_after_menu = InlineKeyboardMarkup(inline_keyboard=[[b_buy_number, b_replenishment],
                                                        [b_rent, b_multiservic],
                                                        [b_history, b_favourites],
                                                        [b_referrals, b_profile]])

b_menu = KeyboardButton(text='🏠 Меню')
b_info = KeyboardButton(text='ℹ Инфо')

start_user_menu = ReplyKeyboardMarkup(keyboard=[[b_menu, b_info]], one_time_keyboard=True, resize_keyboard=True)
