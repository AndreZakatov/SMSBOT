from aiogram.fsm.state import default_state
from aiogram.types import Message
from aiogram import Router, Bot, F
from aiogram.filters import CommandStart, StateFilter

from Config.config import allowed_admin_ids
from Keyboards.start_admin_kb import kb_start_admin
from Keyboards.start_user_kb import start_user_menu, user_after_menu

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
                                    f'🧐 Если возникнут вопросы обращайтесь в поддержку', reply_markup=start_user_menu)


@start_command_router.message(F.text == '🏠 Меню')
async def press_balance(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, text='⬇ Выберете действие ⬇', reply_markup=user_after_menu)