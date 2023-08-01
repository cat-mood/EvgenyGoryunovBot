import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Test message")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
