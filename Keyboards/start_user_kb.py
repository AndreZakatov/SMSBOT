from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

b_balance = KeyboardButton(text='🏦 Баланс')
b_buy_number = KeyboardButton(text='📲 Купить')
b_replenishment = KeyboardButton(text='💸 Пополнение')
b_rent = KeyboardButton(text='⏰ Арендовать')
b_multiservice = KeyboardButton(text='💾 История')
b_history = KeyboardButton(text='🎁 Создание промокода')
b_favourites = KeyboardButton(text='✨ Избранное')
b_referrals = KeyboardButton(text='👥 Рефералы')
b_profile = KeyboardButton(text='🎩 Профиль')

kb_start_user = ReplyKeyboardMarkup(keyboard=[[b_balance, b_buy_number, b_replenishment, b_rent],
                                               [b_multiservice, b_history, b_favourites],
                                               [b_referrals, b_profile]])










