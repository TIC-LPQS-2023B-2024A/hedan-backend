import os

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker


def create_async_session() -> async_sessionmaker[AsyncSession]:
    url: str = os.getenv("DATABASE_URL")
    engine = create_async_engine(url)
    session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    return session
