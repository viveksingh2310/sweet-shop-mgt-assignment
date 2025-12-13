import pytest
import uuid
from httpx import AsyncClient, ASGITransport
from asgi_lifespan import LifespanManager
from sqlalchemy import select

from app.main import app
from app.db.database import AsyncSessionLocal
from app.users.models import User


@pytest.mark.asyncio
async def test_password_is_hashed_before_persisting():
    email = f"user_{uuid.uuid4()}@example.com"
    plain_password = "supersecret123"
    payload = {
        "email": email,
        "password": plain_password,
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
            select(User).where(User.email == email)
        )
        user = result.scalar_one()

        assert user.password != plain_password
