import pytest
from sqlalchemy import text
from app.db.database import engine, DATABASE_URL

@pytest.mark.asyncio
async def test_database_connection():
    assert DATABASE_URL is not None, "DATABASE_URL not set"

    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT 1"))
        assert result.scalar() == 1
