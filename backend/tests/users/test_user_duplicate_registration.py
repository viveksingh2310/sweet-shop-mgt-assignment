import pytest
import uuid
from httpx import AsyncClient, ASGITransport
from asgi_lifespan import LifespanManager

from app.main import app


@pytest.mark.asyncio
async def test_registering_duplicate_email_returns_409():
    email = f"user_{uuid.uuid4()}@example.com"

    payload = {
        "email": email,
        "password": "strongpassword123",
    }

    async with LifespanManager(app):
        transport = ASGITransport(app=app)

        async with AsyncClient(
            transport=transport,
            base_url="http://test",
        ) as client:
            first_response = await client.post(
                "/api/auth/register",
                json=payload,
            )
            assert first_response.status_code == 201
            second_response = await client.post(
                "/api/auth/register",
                json=payload,
            )

    assert second_response.status_code == 409
    assert second_response.json()["detail"] == "Email already registered"
