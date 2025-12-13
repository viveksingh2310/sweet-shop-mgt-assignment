import uuid
import pytest
from httpx import AsyncClient, ASGITransport
from asgi_lifespan import LifespanManager

from app.main import app

@pytest.mark.asyncio
async def test_user_can_login_with_valid_credentials():
    email = f"user_{uuid.uuid4()}@example.com"
    password = "strongpassword123"

    async with LifespanManager(app):
        transport = ASGITransport(app=app)

        async with AsyncClient(
            transport=transport,
            base_url="http://test",
        ) as client:
            # Register user first
            await client.post(
                "/api/auth/register",
                json={"email": email, "password": password},
            )

            # Attempt login
            response = await client.post(
                "/api/auth/login",
                json={"email": email, "password": password},
            )

    assert response.status_code == 200
    assert "access_token" in response.json()
