import asyncio
from aiogram import Bot, Dispatcher

from handlers import command, weather, base, gpt, download
from config_reader import config

bot: Bot = Bot(token=config.bot_token.get_secret_value())
dp: Dispatcher = Dispatcher()


# Запуск бота
async def main():

    dp.include_routers(
        command.router,
        base.router,
        gpt.router,
        weather.router,
        download.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
