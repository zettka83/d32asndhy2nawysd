from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)

from sqlalchemy.orm import DeclarativeBase

from app.utils.config import settings


engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False,
)

Session = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass


async def get_session():
    async with Session() as session:
        yield session