import pytest_asyncio
import uuid
from httpx import AsyncClient, ASGITransport
from asgi_lifespan import LifespanManager
from app.main import app
@pytest_asyncio.fixture
async def admin_token():
    email = f"admin_{uuid.uuid4()}@example.com"
    password = "adminpassword123"

    async with LifespanManager(app):
        async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://test",
        ) as client:
            # Register admin
            await client.post(
                "/api/auth/register",
                json={
                    "email": email,
                    "password": password,
                    "role": "admin",
                },
            )

            # Login admin
            response = await client.post(
                "/api/auth/login",
                json={
                    "email": email,
                    "password": password,
                },
            )

    return response.json()["access_token"]


@pytest_asyncio.fixture
async def user_token():
    email = f"user_{uuid.uuid4()}@example.com"
    password = "userpassword123"

    async with LifespanManager(app):
        async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://test",
        ) as client:
            # Register user
            await client.post(
                "/api/auth/register",
                json={
                    "email": email,
                    "password": password,
                },
            )

            # Login user
            response = await client.post(
                "/api/auth/login",
                json={
                    "email": email,
                    "password": password,
                },
            )

    return response.json()["access_token"]
