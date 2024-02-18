from aiogram.types import Message
from aiogram import Router, Bot, F


admin_command_router = Router()


@admin_command_router.message(F.text == '📊 Статистика')
async def press_statistics(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id,
                           text='Сбор статистики')


@admin_command_router.message(F.text == '📤 Рассылка')
async def press_mailing(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id,
                           text='Произвожу рассылку')


@admin_command_router.message(F.text == '💵 Настройка наценки')
async def press_margin(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id,
                           text='Укажите % наценки')


@admin_command_router.message(F.text == '⌨ Рекламные кнопки')
async def press_advertising(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id,
                           text='Настраиваем рекламные кнопки')


@admin_command_router.message(F.text == '🔍 Поиск пользователя')
async def press_search_user(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id,
                           text='Введите id пользователя')


@admin_command_router.message(F.text == '🎁 Создание промокода')
async def press_create_promo(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id,
                           text='Создаю промокод')
