from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.types import CallbackQuery

from Keyboards.pagination_country import generate_keyboard, keyboard

user_pay_router = Router()


@user_pay_router.message(F.data.in_ == ['pay'])
async def process_start_pay(call: CallbackQuery, message: Message, bot: Bot):
    await bot.send_message(message.from_user.id,
                           text='Выберете страну', reply_markup=keyboard)
