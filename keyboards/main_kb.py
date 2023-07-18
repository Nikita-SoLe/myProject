from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


# Клавиатура главного меню
def get_main_keyboard() -> ReplyKeyboardMarkup:

    kb: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
    kb.button(text='Погода')
    kb.button(text='ChatGPT')
    kb.button(text='Скачать из YouTube')
    kb.adjust(2)

    return kb.as_markup(resize_keyboard=True)


# Клавиатура "Главное меню"
def main_menu_kb() -> ReplyKeyboardMarkup:

    kb: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
    kb.button(text='Главное меню')
    kb.adjust(1)

    return kb.as_markup(resize_keyboard=True)


# Клавиатура скачивания
def get_download_kb() -> ReplyKeyboardMarkup:

    kb: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
    kb.button(text='Видео')
    kb.button(text='Аудио')
    kb.button(text='Главное меню')
    kb.adjust(2)

    return kb.as_markup(resize_keyboard=True)


# Клавиатура меню погоды
def weather_keyboard() -> ReplyKeyboardMarkup:

    kb: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
    kb.button(text='Город')
    kb.button(text='Геолокация', request_location=True)
    kb.button(text='Главное меню')
    kb.adjust(2)

    return kb.as_markup(resize_keyboard=True)
