from aiogram import Router, F
from aiogram.types import Message
from app.database.repository import Repository

router = Router()

@router.message(F.text == "🎁 Магазин")
async def shop_menu(message: Message):
    user = await Repository.get_user(message.from_user.id)
    shop = await Repository.get_shop()
    
    if user.stars >= shop.gift_price:
        await Repository.remove_stars(message.from_user.id, shop.gift_price)
        await Repository.create_exchange(message.from_user.id, shop.gift_name, shop.gift_price)
        await message.answer(f"Поздравляю! Вы купили {shop.gift_name} за {shop.gift_price}⭐")
    else:
        await message.answer(f"У вас недостаточно звезд. Нужно {shop.gift_price}⭐, а у вас {user.stars}⭐")