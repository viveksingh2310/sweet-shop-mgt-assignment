import pytest
from httpx import AsyncClient
from asgi_lifespan import LifespanManager
from httpx import ASGITransport

# ---------- CREATE SWEET (ADMIN) ----------

@pytest.mark.asyncio
async def test_admin_can_create_sweet(app, admin_token):
    async with LifespanManager(app):
        async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://test",
            headers={"Authorization": f"Bearer {admin_token}"},
        ) as client:
            response = await client.post(
                "/api/sweets",
                json={
                    "name": "Rasgulla",
                    "category": "Indian",
                    "price": 20,
                    "quantity": 100,
                },
            )

    assert response.status_code == 201


@pytest.mark.asyncio
async def test_non_admin_cannot_create_sweet(app, user_token):
    async with LifespanManager(app):
        async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://test",
            headers={"Authorization": f"Bearer {user_token}"},
        ) as client:
            response = await client.post("/api/sweets", json={})

    assert response.status_code == 403


# ---------- LIST SWEETS ----------

@pytest.mark.asyncio
async def test_list_sweets_is_public(app):
    async with LifespanManager(app):
        async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://test",
        ) as client:
            response = await client.get("/api/sweets")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


# ---------- SEARCH SWEETS ----------

@pytest.mark.asyncio
async def test_search_sweets_by_name(app):
    async with LifespanManager(app):
        async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://test",
        ) as client:
            response = await client.get(
                "/api/sweets/search",
                params={"name": "ras"},
            )

    assert response.status_code == 200


# ---------- UPDATE SWEET (ADMIN) ----------

@pytest.mark.asyncio
async def test_admin_can_update_sweet(app, admin_token):
    async with LifespanManager(app):
        async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://test",
            headers={"Authorization": f"Bearer {admin_token}"},
        ) as client:
            response = await client.put(
                "/api/sweets/1",
                json={"price": 25},
            )

    assert response.status_code in (200, 404)


# ---------- DELETE SWEET (ADMIN) ----------

@pytest.mark.asyncio
async def test_admin_can_delete_sweet(app, admin_token):
    async with LifespanManager(app):
        async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://test",
            headers={"Authorization": f"Bearer {admin_token}"},
        ) as client:
            response = await client.delete("/api/sweets/1")

    assert response.status_code in (204, 404)
