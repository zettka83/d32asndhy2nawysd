import asyncio
from app.database.db import engine, Base
from app.database.models import User, Question, UserAnswer, StarHistory, Referral, Shop, Exchange, Setting, Admin
from app.database.repository import Repository

async def init_tables():
    print("Создаю таблицы...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Таблицы успешно созданы.")

    # Добавляем тестовый вопрос
    await Repository.add_question("general", "Сколько звезд на небе? (пиши '5')", "5", 1)
    print("Тестовый вопрос добавлен.")

if __name__ == "__main__":
    asyncio.run(init_tables())