from aiogram import Router
from aiogram.filters.text import Text
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from fsm.base import FSM_Main
from keyboards.main_kb import get_main_keyboard, main_menu_kb, get_download_kb, weather_keyboard


router: Router = Router()


# Хэндлер на кнопку Погода
@router.message(Text('Погода'))
async def get_weather_kb(message: Message, state: FSMContext):
    await message.answer(
        "Где бы вы хотели узнать погоду?",
        reply_markup=weather_keyboard()
    )
    await state.set_state(FSM_Main.weather)


# Хэндлер на кнопку ChatGPT
@router.message(Text('ChatGPT'))
async def gpt_button_touch(message: Message, state: FSMContext):
    await state.set_state(FSM_Main.chat_gpt)
    await message.answer(
        f'Привет, я ChatGPT\n '
        f'👋\n'
        f'Что ты хочешь у меня узнать?',
        reply_markup=main_menu_kb(),

    )


# Хэндлер на кнопку скачивания
@router.message(Text('Скачать из YouTube'))
async def download_for_yt(message: Message, state: FSMContext):
    await state.set_state(FSM_Main.download)
    await message.answer(
        text='Вы можете скачать видео с YouTube\n'
             'Или аудиодорожку из видео на YouTube\n',
        reply_markup=get_download_kb()
    )


# Хэндлер на кнопку Главное меню
@router.message(Text('Главное меню'))
async def main_menu(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Главное меню',
                         reply_markup=get_main_keyboard())
