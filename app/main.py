from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()


bot =Bot(os.getenv("BOT_TOKEN"))

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand(
                command="start",
                description="Запустити телеграм бот"
            ),

            types.BotCommand(
                command="stop",
                description="Зупинити бот"
            )
        ]
    )

executor.start_polling(dp)
