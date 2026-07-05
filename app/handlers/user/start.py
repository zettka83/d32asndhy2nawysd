from aiogram import Router
from aiogram.filters import CommandStart, CommandObject
from aiogram.types import Message

from app.database.repository import Repository
from app.keyboards.reply import main_menu

router = Router()


@router.message(CommandStart())
async def start_command(
    message: Message,
    command: CommandObject
):
    user = await Repository.get_user(message.from_user.id)

    # Пользователь уже существует
    if user:
        await message.answer(
            f"👋 С возвращением, <b>{message.from_user.first_name}</b>!",
            reply_markup=main_menu
        )
        return

    # Создаем пользователя
    await Repository.create_user(
        tg_id=message.from_user.id,
        full_name=message.from_user.full_name,
        username=message.from_user.username
    )

    # Проверяем реферальную ссылку
    if command.args:

        try:
            inviter_id = int(command.args)

            # Чтобы нельзя было пригласить самого себя
            if inviter_id != message.from_user.id:

                # Проверяем, что бонус ещё не получен
                exists = await Repository.referral_exists(
                    message.from_user.id
                )

                if not exists:

                    await Repository.add_referral(
                        inviter_id=inviter_id,
                        invited_id=message.from_user.id
                    )

                    await Repository.increase_invited(inviter_id)

                    await Repository.add_stars(
                        inviter_id,
                        1
                    )

        except ValueError:
            pass

    await message.answer(
        f"🎉 Добро пожаловать, <b>{message.from_user.first_name}</b>!\n\n"
        "⭐ Выполняйте задания и получайте звезды.\n"
        "🎁 Обменивайте их на Telegram-подарки.",
        reply_markup=main_menu
    )