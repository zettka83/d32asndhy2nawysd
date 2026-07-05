from datetime import datetime

from sqlalchemy import (
    String,
    Integer,
    Boolean,
    DateTime,
    Text,
)

from sqlalchemy.orm import Mapped, mapped_column

from app.database.db import Base


# ==========================================
# Пользователи
# ==========================================

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    tg_id: Mapped[int] = mapped_column(Integer, unique=True)

    full_name: Mapped[str] = mapped_column(String(255))

    username: Mapped[str | None] = mapped_column(String(100), nullable=True)

    stars: Mapped[int] = mapped_column(Integer, default=0)

    invited: Mapped[int] = mapped_column(Integer, default=0)

    referral_stars: Mapped[int] = mapped_column(Integer, default=0)

    solved_questions: Mapped[int] = mapped_column(Integer, default=0)

    blocked: Mapped[bool] = mapped_column(Boolean, default=False)

    register_date: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )


# ==========================================
# Вопросы
# ==========================================

class Question(Base):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(primary_key=True)

    subject: Mapped[str] = mapped_column(String(100))

    question: Mapped[str] = mapped_column(Text)

    answer: Mapped[str] = mapped_column(Text)

    stars: Mapped[int] = mapped_column(Integer, default=1)


# ==========================================
# Решенные вопросы
# ==========================================

class UserAnswer(Base):
    __tablename__ = "user_answers"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(Integer)

    question_id: Mapped[int] = mapped_column(Integer)


# ==========================================
# История начислений
# ==========================================

class StarHistory(Base):
    __tablename__ = "star_history"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(Integer)

    amount: Mapped[int] = mapped_column(Integer)

    reason: Mapped[str] = mapped_column(Text)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )


# ==========================================
# Рефералы
# ==========================================

class Referral(Base):
    __tablename__ = "referrals"

    id: Mapped[int] = mapped_column(primary_key=True)

    inviter_id: Mapped[int] = mapped_column(Integer)

    invited_id: Mapped[int] = mapped_column(Integer)

    reward: Mapped[int] = mapped_column(Integer, default=1)


# ==========================================
# Магазин
# ==========================================

class Shop(Base):
    __tablename__ = "shop"

    id: Mapped[int] = mapped_column(primary_key=True)

    gift_name: Mapped[str] = mapped_column(String(255))

    gift_price: Mapped[int] = mapped_column(Integer)


# ==========================================
# История обменов
# ==========================================

class Exchange(Base):
    __tablename__ = "exchanges"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(Integer)

    gift_name: Mapped[str] = mapped_column(String(255))

    stars: Mapped[int] = mapped_column(Integer)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )


# ==========================================
# Настройки
# ==========================================

class Setting(Base):
    __tablename__ = "settings"

    key: Mapped[str] = mapped_column(
        String(100),
        primary_key=True
    )

    value: Mapped[str] = mapped_column(Text)


# ==========================================
# Администраторы
# ==========================================

class Admin(Base):
    __tablename__ = "admins"

    id: Mapped[int] = mapped_column(primary_key=True)

    tg_id: Mapped[int] = mapped_column(Integer, unique=True)