from aiogram import Router, F
from aiogram.types import Message

from app.database.repository import Repository

router = Router()


@router.message(F.text == "⭐ Мой баланс")
async def balance(message: Message):

    user = await Repository.get_user(
        message.from_user.id
    )

    shop = await Repository.get_shop()

    left = max(0, shop.gift_price - user.stars)

    await message.answer(
        f"⭐ <b>Ваш баланс:</b> {user.stars}\n\n"
        f"🎁 До подарка осталось:\n"
        f"<b>{left} ⭐</b>\n\n"
        f"👥 Приглашено друзей: <b>{user.invited}</b>"
    )