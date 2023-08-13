from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def start_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="/appointment")
    kb.button(text="/view")
    kb.button(text="/cancel")
    kb.button(text="/archive")
    kb.button(text="/message")
    kb.adjust(5)
    return kb.as_markup(resize_keyboard=True, input_field_placeholder = "Выберите вашу услугу")
