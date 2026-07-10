from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from src.keyboards import inline_2, inline, CallbackQuery
from src.questions import QUESTIONS
from db.users import create_user, get_user
from db.questions import (add_question, 
                          get_all_questions,
                          delete_question)
from db.results import get_score, save_result

router = Router()

class Quiz(StatesGroup):
    waiting_answer = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    user = create_user(
        telegram_id = message.from_user.id,
        username= message.from_user.username or "Unknown"
    )
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


'''---HOMEWORK #5 ---'''
@router.message(Command('list'))
async def cmd_list(message:Message):
    questions = get_all_questions()
    if not questions:
        await message.answer("Пока нет вопросов")
        return 
    
    lines = []
    lines.append("Список всех вопросов:\n")
    
    for r in questions:
        id = r[0]
        text = r[1]
        answer = r[2]
        lines.append(f"{id}. Вопрос: {text} / Ответ: {answer}")

    full_message = "\n".join(lines)
    await message.answer(full_message)

@router.message(Command("add"))
async def cmd_add(message: Message):
    text_parts = message.text.split()
    if len(text_parts) < 3:
        await message.answer("Напишите : /add Вопрос Ответ")
        return
        
    question_text = text_parts[1]
    correct_answer = text_parts[2]

    add_question(question_text, correct_answer)
    await message.answer("Вопрос добавлен!")


@router.message(Command("del"))
async def cmd_del(message: Message):
    text_parts = message.text.split()
    if len(text_parts) < 2:
        await message.answer("Напиши ID. Пример: /del 5")
        return
        
    question_id = int(text_parts[1]) 
    delete_question(question_id)
    await message.answer(f"Вопрос с ID {question_id} удален!")

#homework #4 
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