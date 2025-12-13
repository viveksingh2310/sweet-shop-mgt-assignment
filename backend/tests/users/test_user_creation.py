import pytest
from httpx import AsyncClient, ASGITransport
from sqlalchemy import select
from asgi_lifespan import LifespanManager
import uuid
from app.main import app
from app.db.database import AsyncSessionLocal, engine
from app.users.models import User


@pytest.mark.asyncio
async def test_user_is_persisted_in_database():
    payload = {
    "email": f"user_{uuid.uuid4()}@example.com",
    "password": "strongpassword123",
}

    async with LifespanManager(app):
        transport = ASGITransport(app=app)

        async with AsyncClient(
            transport=transport,
            base_url="http://test",
        ) as client:
            response = await client.post(
                "/api/auth/register",
                json=payload,
            )

    assert response.status_code == 201

    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(User).where(User.email == payload["email"])
        )
        user = result.scalar_one_or_none()

    assert user is not None
    assert user.email == payload["email"]
    await engine.dispose()
