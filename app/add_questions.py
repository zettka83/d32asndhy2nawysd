import asyncio
from app.database.repository import Repository

async def main():
    # Список вопросов для добавления
    questions = [
        {
            "subject": "general",
            "question": "Сколько звезд на небе? (шучу, напиши '5')",
            "answer": "5",
            "stars": 1
        },
        {
            "subject": "general",
            "question": "Какой язык программирования использует этот бот? (aiogram/...)",
            "answer": "python",
            "stars": 1
        }
    ]
    
    for q in questions:
        await Repository.add_question(
            subject=q["subject"],
            question=q["question"],
            answer=q["answer"],
            stars=q["stars"]
        )
        print(f"Вопрос добавлен: {q['question']}")

if __name__ == "__main__":
    asyncio.run(main())