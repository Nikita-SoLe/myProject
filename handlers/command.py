from aiogram import Router, Bot, types
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.main_kb import get_main_keyboard
from config_reader import config

router: Router = Router()


# Хэндлер для команды старт
@router.message(Command('start'))
async def command_start(message: Message):
    await message.answer(
        text=f'Привет, {message.from_user.first_name}\n'
             f'Я умею показывать погоду и в меня встроен умный помощник',
        reply_markup=get_main_keyboard()
    )


# Хендлер для команды хелп
@router.message(Command('help'))
async def command_help(message: Message):
    pass


# Обработка платежа
@router.message(Command('buy'))
async def command_buy(message: Message, bot: Bot):
    # amount должен получать сумму в копейках
    PRICE = types.LabeledPrice(label='Подписка на 1 месяц', amount=10*100)
    if config.pay_token.get_secret_value().split(':')[1] == 'TEST':
        await bot.send_invoice(message.chat.id,
                               title='Подписка на бота',
                               description='Активация подписки на 1 месяц',
                               provider_token=config.pay_token.get_secret_value(),
                               currency='RUB',
                               photo_url='https://th.bing.com/th/id/OIP.uED5lS9AgKQ5Wg3bprLfjQHaHa?w=172&h=180&c=7&r=0&o=5&pid=1.7',
                               photo_width=416,
                               photo_height=234,
                               photo_size=416,
                               is_flexible=False,
                               prices=[PRICE],
                               start_parameter='one-month-subscription',
                               payload='test-invoice-payload')
