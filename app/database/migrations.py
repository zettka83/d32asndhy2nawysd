from sqlalchemy import select

from app.database.db import engine, Session, Base
from app.database.models import Shop, Setting, Admin
from app.utils.config import settings


async def create_database():
    # Создаем все таблицы
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Заполняем таблицы по умолчанию
    async with Session() as session:

        # -----------------------------
        # Магазин
        # -----------------------------
        shop = await session.scalar(
            select(Shop)
        )

        if shop is None:
            session.add(
                Shop(
                    gift_name="🐻 Telegram-подарок «Мишка»",
                    gift_price=15
                )
            )

        # -----------------------------
        # Настройки
        # -----------------------------
        settings_data = {
            "welcome_text": (
                "👋 Добро пожаловать!\n\n"
                "📚 Решайте задания\n"
                "⭐ Получайте звезды\n"
                "🎁 Обменивайте их на подарки."
            ),
            "rules": (
                "📜 Правила\n\n"
                "• Не используйте несколько аккаунтов.\n"
                "• Не пытайтесь взломать бота.\n"
                "• За нарушение правил аккаунт может быть заблокирован."
            ),
            "gift_price": "15",
            "referral_reward": "1",
            "referral_bonus": "5"
        }

        for key, value in settings_data.items():

            exists = await session.scalar(
                select(Setting).where(
                    Setting.key == key
                )
            )

            if exists is None:
                session.add(
                    Setting(
                        key=key,
                        value=value
                    )
                )

        # -----------------------------
        # Администратор
        # -----------------------------
        admin = await session.scalar(
            select(Admin).where(
                Admin.tg_id == settings.ADMIN_IDS
            )
        )

        if admin is None:
            session.add(
                Admin(
                    tg_id=settings.ADMIN_IDS
                )
            )

        await session.commit()