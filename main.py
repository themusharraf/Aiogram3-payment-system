from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery
from root import Payments_Token


async def order(message: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=message.chat_id,
        title="Order alert Telegram bot",
        description="Order alert Telegram bot price product payment ",
        payload="Payment bot orqali",  # noqa
        provider_token=Payments_Token,
        currency="sum",
        prices=[
            LabeledPrice(
                label="discount",
                amount=-2000,

            ),
            LabeledPrice(
                label="Bonus",
                amount=-1500,

            )
        ],
        max_tip_amount=5000,
        suggested_tip_amounts=[1000, 2000, 4000],
        start_parameter="ALL NC",
        provider_data=None,
        photo_url="https://images.uzum.uz/cm3b39taqb253442d710/original.jpg",
        photo_size=100,
        photo_width=800,
        photo_height=450,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=False,
        send_phone_number_to_provider=False,
        send_email_to_provider=False,
        is_flexible=False,
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        reply_markup=None,
        request_timeout=15

    )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot): # noqa
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)
