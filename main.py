import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

BOT_TOKEN = "8800511811:AAEAHpYSkuZWTWY2AfQXaJ_BBbqO39RQSrM"


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()     # обработчик входящих обновлений

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! Я твой первый бот."
        )

@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(
        '/start - приветствие\n'
        '/help - список команд'
    )

@dp.message(Command('about'))
async def cmd_about(message: Message):
    await message.answer(
        f"Этот бот создан как тестовый образец."
    )

async def main():
    await dp.start_polling(bot)     # отправляет запросы на тг-сервер


if __name__ == "__main__":
    asyncio.run(main())
