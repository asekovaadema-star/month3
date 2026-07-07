from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from src.keyboards import inline_2, inline, CallbackQuery
from src.questions import QUESTIONS

router = Router()

class Quiz(StatesGroup):
    waiting_answer = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! Я твой первый бот."
        )
    print(f'Пользователь {message.from_user.full_name}')

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(
        '/start - приветствие\n'
        '/help - документация к языкам\n'
        '/game -  запускает викторину'
        , reply_markup=inline
    )

@router.message(Command('about'))
async def cmd_about(message: Message):
    await message.answer(
        f"Этот бот создан как тестовый образец."
    )

@router.message(Command("game"))
async def cmd_game(message: Message):
    await message.answer(
        f"Выберите один пункт:", reply_markup= inline
    )

@router.callback_query(F.data == 'quiz_start')
async def start_quiz(callback: CallbackQuery, state: FSMContext):
    await callback.answer('Начинаем игру!', show_alert=True)
    await state.update_data(index=0, score=0)
    await state.set_state(Quiz.waiting_answer)
    await callback.message.answer(f"Вопрос 1: {QUESTIONS[0]['q']}")


@router.message(Quiz.waiting_answer)  
async def handle_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    index = data['index']
    score = data['score']

    if message.text.lower() == QUESTIONS[index]['a']:
        score += 1
        await message.answer("Правильно! +1")
    else:
        await message.answer(f"Неправильно. Правильный ответ: {QUESTIONS[index]['a']}")
    
    index += 1

    if index >= len(QUESTIONS):
        await message.answer(f"Конец! Счет: {score}/{len(QUESTIONS)}", reply_markup=inline_2)
        await state.clear()
    else:
        await state.update_data(index=index, score=score)
        await message.answer(f"Вопрос {index+1}: {QUESTIONS[index]['q']}")

@router.callback_query(F.data == "play_again")
async def restart_quiz(callback: CallbackQuery, state: FSMContext):
    await callback.answer("Играем снова", show_alert= True)
    await callback.message.answer("Начали повторно викторину")
    await state.set_state(Quiz.waiting_answer)
    await callback.message.answer(f"Вопрос 1: {QUESTIONS[0]['q']}")

#FSM - Final State Machine