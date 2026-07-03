from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardButton,
                           InlineKeyboardMarkup, 
                           CallbackQuery)

keyboard_start= ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Python")],
    [KeyboardButton(text="JS"), KeyboardButton(text="C#")]
], resize_keyboard=True, input_field_placeholder="Выберите один язык")


inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Python", 
    url="https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://docs.python.org/&ved=2ahUKEwiumfiaqraVAxVoSvEDHUndEpUQFnoECB0QAQ&usg=AOvVaw0eRfv-QpH-JIna_jepcnW7", 
    callback_data="python")],
    [InlineKeyboardButton(text= "JS",
    url = "https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://developer.mozilla.org/ru/docs/Web/JavaScript&ved=2ahUKEwiS8IGzqraVAxVlVfEDHTMSCXQQFnoECCIQAQ&usg=AOvVaw1ljaIJ9AnrbHsJiFJdpQBB",
    callback_data="js")],
    [InlineKeyboardButton(text="C#",
    url ="https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://learn.microsoft.com/ru-ru/dotnet/csharp/&ved=2ahUKEwjm07ruqraVAxX9QvEDHXyYJWAQFnoECA0QAQ&usg=AOvVaw3HdWXu3XtZTS0gNtv1WTk6",
    callback_data="c#")],
    [InlineKeyboardButton(text= "Начать обучение", callback_data="start_lern")]
])

