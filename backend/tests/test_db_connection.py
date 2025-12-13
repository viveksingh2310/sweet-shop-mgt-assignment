import os
import pytest
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
from sqlalchemy.exc import OperationalError

load_dotenv()

@pytest.mark.asyncio
async def test_database_connection():
    DATABASE_URL = os.getenv("DATABASE_URL")
    assert DATABASE_URL is not None, "DATABASE_URL not set"

    engine = create_async_engine(DATABASE_URL)

    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT 1"))
        assert result.scalar() == 1