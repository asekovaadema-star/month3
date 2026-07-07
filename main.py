import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.fsm.storage.memory import MemoryStorage
from src.handlers import router

from config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())     # обработчик входящих обновлений

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)     # отправляет запросы на тг-сервер


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())