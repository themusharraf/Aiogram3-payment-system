import asyncio
import logging
import random

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import types
from root import TOKEN

logging.basicConfig(level=logging.INFO)

myToken = TOKEN
bot = Bot(token=myToken, parse_mode="HTML")
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.reply(f" <b>{message.from_user.first_name}</b> sizga qanday yordam bera olaman  <u>  </u> ",
                        parse_mode="HTML")


@dp.message(Command("location"))
async def location(message: Message):
    key = [
        [types.KeyboardButton(text="location", request_location=True)],
        [types.KeyboardButton(text="contact", request_contact=True)],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=key, resize_keyboard=True)
    await message.answer("location or contact", reply_markup=keyboard)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
