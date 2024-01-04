from aiogram import Bot
from aiogram.types import Message, LabeledPrice


async def order(message: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=message.chat_id,
        title="Order alert Telegram bot",
        description="Order alert Telegram bot price product payment ",
        payload="Payment bot orqali", # noqa
    )
