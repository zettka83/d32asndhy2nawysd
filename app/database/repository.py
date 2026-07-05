from sqlalchemy import select, update, func
from app.database.db import Session
from app.database.models import (
    User,
    Question,
    UserAnswer,
    Shop,
    Referral,
    StarHistory,
    Exchange
)


class Repository:

    # -------------------------
    # Пользователи
    # -------------------------

    @staticmethod
    async def get_user(tg_id: int):
        async with Session() as session:
            return await session.scalar(
                select(User).where(User.tg_id == tg_id)
            )

    @staticmethod
    async def create_user(
        tg_id: int,
        full_name: str,
        username: str | None
    ):
        async with Session() as session:

            user = User(
                tg_id=tg_id,
                full_name=full_name,
                username=username,
            )

            session.add(user)

            await session.commit()

            return user

    @staticmethod
    async def add_stars(
        tg_id: int,
        stars: int,
        reason: str = "Правильный ответ"
    ):
        async with Session() as session:

            await session.execute(
                update(User)
                .where(User.tg_id == tg_id)
                .values(
                    stars=User.stars + stars,
                    solved_questions=User.solved_questions + 1
                )
            )

            history = StarHistory(
                user_id=tg_id,
                amount=stars,
                reason=reason
            )

            session.add(history)

            await session.commit()

    @staticmethod
    async def remove_stars(
        tg_id: int,
        stars: int
    ):
        async with Session() as session:

            await session.execute(
                update(User)
                .where(User.tg_id == tg_id)
                .values(
                    stars=User.stars - stars
                )
            )

            await session.commit()

    @staticmethod
    async def get_top():

        async with Session() as session:

            result = await session.scalars(
                select(User)
                .order_by(User.stars.desc())
                .limit(10)
            )

            return result.all()

    # -------------------------
    # Вопросы
    # -------------------------

    @staticmethod
    async def get_random_question(subject: str):

        async with Session() as session:

            result = await session.scalar(
                select(Question)
                .where(Question.subject == subject)
                .order_by(func.random())
            )

            return result

    @staticmethod
    async def get_question(question_id: int):

        async with Session() as session:

            return await session.scalar(
                select(Question)
                .where(Question.id == question_id)
            )

    @staticmethod
    async def add_question(
        subject: str,
        question: str,
        answer: str,
        stars: int
    ):

        async with Session() as session:

            q = Question(
                subject=subject,
                question=question,
                answer=answer.lower().strip(),
                stars=stars
            )

            session.add(q)

            await session.commit()

    # -------------------------
    # Решенные вопросы
    # -------------------------

    @staticmethod
    async def answer_exists(
        user_id: int,
        question_id: int
    ):

        async with Session() as session:

            result = await session.scalar(
                select(UserAnswer)
                .where(
                    UserAnswer.user_id == user_id,
                    UserAnswer.question_id == question_id
                )
            )

            return result is not None

    @staticmethod
    async def save_answer(
        user_id: int,
        question_id: int
    ):

        async with Session() as session:

            answer = UserAnswer(
                user_id=user_id,
                question_id=question_id
            )

            session.add(answer)

            await session.commit()

    # -------------------------
    # Магазин
    # -------------------------

    @staticmethod
    async def get_shop():

        async with Session() as session:

            return await session.scalar(
                select(Shop)
            )

    # -------------------------
    # Рефералы
    # -------------------------

    @staticmethod
    async def add_referral(
        inviter_id: int,
        invited_id: int
    ):

        async with Session() as session:

            referral = Referral(
                inviter_id=inviter_id,
                invited_id=invited_id
            )

            session.add(referral)

            await session.commit()

    @staticmethod
    async def referral_exists(
        invited_id: int
    ):

        async with Session() as session:

            result = await session.scalar(
                select(Referral)
                .where(
                    Referral.invited_id == invited_id
                )
            )

            return result is not None

    @staticmethod
    async def increase_invited(
        inviter_id: int
    ):

        async with Session() as session:

            await session.execute(
                update(User)
                .where(User.tg_id == inviter_id)
                .values(
                    invited=User.invited + 1,
                    referral_stars=User.referral_stars + 1,
                    stars=User.stars + 1
                )
            )

            await session.commit()

    # -------------------------
    # Обмен подарков
    # -------------------------

    @staticmethod
    async def create_exchange(
        user_id: int,
        gift_name: str,
        stars: int
    ):

        async with Session() as session:

            exchange = Exchange(
                user_id=user_id,
                gift_name=gift_name,
                stars=stars
            )

            session.add(exchange)

            await session.commit()