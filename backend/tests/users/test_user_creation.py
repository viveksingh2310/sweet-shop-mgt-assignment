import pytest
from fastapi.testclient import TestClient
from sqlalchemy import select
from app.main import app
from app.db.database import AsyncSessionLocal
from app.users.models import User

client = TestClient(app)


def test_user_is_persisted_in_database():
    payload = {
        "email": "persisted_user@example.com",
        "password": "strongpassword123",
    }

    response = client.post("/api/auth/register", json=payload)

    assert response.status_code == 201

    async def check_user_in_db():
        async with AsyncSessionLocal() as session:
            result = await session.execute(
                select(User).where(User.email == payload["email"])
            )
            return result.scalar_one_or_none()

    user = pytest.run(check_user_in_db())

    assert user is not None
    assert user.email == payload["email"]
