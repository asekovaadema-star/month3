from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardButton,
                           InlineKeyboardMarkup, 
                           CallbackQuery)

inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text= "Начать винторину", callback_data="quiz_start")], 
    [InlineKeyboardButton(text="Мой счет", callback_data="My score")]
])

inline_2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text= "Сыграть снова", callback_data="play_again")]
])