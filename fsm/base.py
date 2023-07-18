from aiogram.fsm.state import StatesGroup, State


# Главные состояния
class FSM_Main(StatesGroup):
    weather = State()
    chat_gpt = State()
    download = State()


class Weather(StatesGroup):
    city = State()


class Download(StatesGroup):
    video = State()
    audio = State()

