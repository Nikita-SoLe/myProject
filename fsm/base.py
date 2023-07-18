from aiogram.fsm.state import StatesGroup, State


# Главные состояния
class FSM_Main(StatesGroup):
    weather = State()
    chat_gpt = State()
    download = State()


# Состояния для меню погоды
class Weather(StatesGroup):
    city = State()


# Состояние для меню скачивания
class Download(StatesGroup):
    video = State()
    audio = State()

