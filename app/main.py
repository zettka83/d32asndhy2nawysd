import asyncio

from aiogram import Dispatcher

from app.bot import bot
from app.database.migrations import create_database
from app.handlers.user import router as user_router
# Если ваш код роутера лежит в app/handlers/admin/handlers.py
from app.handlers.admin.admin import router as admin_router
from app.utils.logger import log


async def start():

    # Создаем таблицы
    await create_database()

    # Создаем диспетчер
    dp = Dispatcher()

    # Подключаем роутеры
    dp.include_router(user_router)
    dp.include_router(admin_router)

    log.info("===================================")
    log.info("Бот успешно запущен!")
    log.info("===================================")

    await dp.start_polling(bot)


def main():
    asyncio.run(start())


if __name__ == "__main__":
    main()