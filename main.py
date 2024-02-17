import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, StateFilter, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand, Message

from Config.config import Config, load_config
from Handlers.start_handler import start_command_router

# Инициализация логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Функция настройки логирования в файл
def setup_logging():
    file_handler = logging.FileHandler(filename='bot_log.txt', mode='w')
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


# Конфигурация логирования и запуск бота
async def main():
    # Конфигурация логирования
    setup_logging()
    logger.info('Bot started')

    # Загрузка конфигурации в переменную
    config: Config = load_config()

    storage = MemoryStorage()
    # Инициализация бота и диспатчера
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    # Команда старт
    dp.include_router(start_command_router)

    # Запуск бесконечного цикла обработки событий
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as e:
        logger.error(f'An error occurred: {e}')