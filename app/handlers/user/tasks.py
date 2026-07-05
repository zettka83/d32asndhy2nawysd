from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from app.database.repository import Repository

router = Router()

class TaskStates(StatesGroup):
    waiting_for_answer = State()

@router.message(F.text == "🔍 Выполнить задание")
async def get_task(message: Message, state: FSMContext):
    # Берем случайный вопрос (предположим, предмет 'general')
    question = await Repository.get_random_question("general")
    if not question:
        await message.answer("Пока нет доступных заданий.")
        return
    
    await state.update_data(question_id=question.id, answer=question.answer)
    await state.set_state(TaskStates.waiting_for_answer)
    await message.answer(f"Вопрос: {question.question}")

@router.message(TaskStates.waiting_for_answer)
async def check_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    if message.text.lower().strip() == data['answer']:
        # Начисляем звезды
        await Repository.add_stars(message.from_user.id, 1, reason="Решение задания")
        await Repository.save_answer(message.from_user.id, data['question_id'])
        await message.answer("Верно! Вы получили 1⭐")
    else:
        await message.answer("Неверно, попробуйте еще раз.")
    await state.clear()