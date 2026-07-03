from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from src.keyboards import keyboard_start, inline, CallbackQuery

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! Я твой первый бот.",
        reply_markup=keyboard_start
        )
    print(f'Пользователь {message.from_user.full_name}')

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(
        '/start - приветствие\n'
        '/help - документация к языкам', reply_markup=inline
    )

@router.message(Command('about'))
async def cmd_about(message: Message):
    await message.answer(
        f"Этот бот создан как тестовый образец."
    )

@router.message(F.text == 'Python')
async def get_group(message: Message):
    await message.answer("Python - это простой язык программирования, с динамичной типизацией, идеальный для новичков.")

@router.message(F.text == 'JS')
async def get_group(message: Message):
    await message.answer("JS (JavaScript) — главный язык веб-разработки для создания интерактивности в браузере.")

@router.message(F.text == 'C#')
async def get_group(message: Message):
    await message.answer("C# — мощный, объектно-ориентированный язык от компании Microsoft со строгой статической типизацией")

@router.callback_query(F.data == "start_lern")
async def process_start_learning(callback: CallbackQuery):
    await callback.answer("Начинаем обучение!",
        show_alert=True
    )

@router.message(F.text.lower () == "группа")
async def get_group(message:Message):
    await message.answer("Твоя группа 67-1")

@router.message(F.text.from_user.id==1094236182)
async def get_group(message:Message):
    await message.answer("Hello the most beautyfull girl")

@router.message(F.text.lower() == "пока")
async def bye(message: Message):
    await message.answer(f"Давай{message.from_user.full_name}связь")