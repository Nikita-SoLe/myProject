from aiogram import Router, F
from aiogram.filters.text import Text
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from config_reader import config
from keyboards.main_kb import main_menu_kb, weather_keyboard
from fsm.base import FSM_Main, Weather
from weather.get_weather import weather_get_city, location_weather
from lexicon.weather import get_weather_text

router: Router = Router()


@router.message(Text('Город'))
async def city_weather(message: Message, state: FSMContext):
    await message.answer(
        'Введите название города',
        reply_markup=main_menu_kb()
    )
    await state.set_state(Weather.city)


@router.message(Weather.city, F.text)
async def city_text_handler(message: Message, state: FSMContext):
    await state.set_state(FSM_Main.weather)

    weather = weather_get_city(message.text, config.api_token.get_secret_value())

    await message.answer(
        get_weather_text(weather),
        reply_markup=weather_keyboard()
    )


@router.message(FSM_Main.weather, F.location)
async def weather_location(message: Message):

    lat = message.location.latitude
    lon = message.location.longitude

    weather = location_weather(lat, lon, config.api_token.get_secret_value())

    await message.answer(
        get_weather_text(weather),
        reply_markup=weather_keyboard()
    )