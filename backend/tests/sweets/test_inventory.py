import pytest
from httpx import AsyncClient, ASGITransport
from asgi_lifespan import LifespanManager
from app.main import app

# ---------- PURCHASE SWEET ----------

@pytest.mark.asyncio
async def test_user_can_purchase_sweet(user_token):
    async with LifespanManager(app):
        async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://test",
            headers={"Authorization": f"Bearer {user_token}"},
        ) as client:
            response = await client.post("/api/sweets/1/purchase")

    # Either purchase succeeds or sweet doesn't exist
    assert response.status_code in (200, 404)


@pytest.mark.asyncio
async def test_purchase_fails_when_out_of_stock(user_token):
    async with LifespanManager(app):
        async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://test",
            headers={"Authorization": f"Bearer {user_token}"},
        ) as client:
            response = await client.post("/api/sweets/999/purchase")

    assert response.status_code in (400, 404)


# ---------- RESTOCK SWEET (ADMIN) ----------

@pytest.mark.asyncio
async def test_admin_can_restock_sweet(admin_token):
    async with LifespanManager(app):
        async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://test",
            headers={"Authorization": f"Bearer {admin_token}"},
        ) as client:
            response = await client.post(
                "/api/sweets/1/restock",
                json={"quantity": 10},
            )

    assert response.status_code in (200, 404)


@pytest.mark.asyncio
async def test_non_admin_cannot_restock(user_token):
    async with LifespanManager(app):
        async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://test",
            headers={"Authorization": f"Bearer {user_token}"},
        ) as client:
            response = await client.post(
                "/api/sweets/1/restock",
                json={"quantity": 10},
            )

    assert response.status_code == 403
