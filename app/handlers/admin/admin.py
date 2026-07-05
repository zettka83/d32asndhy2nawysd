from aiogram import Router, types
from aiogram.filters import Command

# Создаем роутер
router = Router()

# Пример простого хэндлера (команда /admin)
@router.message(Command("admin"))
async def admin_start(message: types.Message):
    await message.answer("Привет, админ! Панель управления работает.")