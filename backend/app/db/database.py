import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
