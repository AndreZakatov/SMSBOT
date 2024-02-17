from aiogram.fsm.state import default_state
from aiogram.types import Message
from aiogram import Router, Bot, F
from aiogram.filters import CommandStart, StateFilter

from Config.config import allowed_admin_ids
from Keyboards.start_admin_kb import kb_start_admin
from Keyboards.start_user_kb import kb_start_user

start_command_router = Router()


@start_command_router.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message, bot: Bot):
    user_id = message.from_user.id
    if user_id in allowed_admin_ids:
        await bot.send_message(message.from_user.id,
                               text=f'Доброго времени суток {message.from_user.first_name}\n\n'
                                    f'Вы вошли в режиме администратора', reply_markup=kb_start_admin)
    else:
        await bot.send_message(message.from_user.id,
                               text=f'👋 Приветствую тебя {message.from_user.username} в SMS_BOT.\n\n'
                                    f'🛒 Приятных покупок!\n\n'
                                    f'🧐 Если возникнут вопросы обращайтесь в поддержку', reply_markup=kb_start_user)


@start_command_router.message(F.text == '📊 Статистика')
async def press_statistics(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id,
                           text='Сбор статистики')


@start_command_router.message(F.text == '📤 Рассылка')
async def press_mailing(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id,
                           text='Произвожу рассылку')


@start_command_router.message(F.text == '💵 Настройка наценки')
async def press_margin(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id,
                           text='Укажите % наценки')


@start_command_router.message(F.text == '⌨ Рекламные кнопки')
async def press_advertising(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id,
                           text='Настраиваем рекламные кнопки')


@start_command_router.message(F.text == '🔍 Поиск пользователя')
async def press_search_user(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id,
                           text='Введите id пользователя')


@start_command_router.message(F.text == '🎁 Создание промокода')
async def press_create_promo(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id,
                           text='Создаю промокод')