from fastapi import APIRouter, Depends, HTTPException
from app.db.database import AsyncSessionLocal
from app.sweets.repository import (
    create_sweet,
    list_sweets,
    search_sweets,
    get_sweet_by_id,
)
from app.users.models import User
from app.core.dependencies import require_admin

router = APIRouter(prefix="/api/sweets", tags=["Sweets"])


# ---------- CREATE SWEET (ADMIN ONLY) ----------
@router.post("", status_code=201)
async def add_sweet(
    payload: dict,
    user: User = Depends(require_admin),
):
    async with AsyncSessionLocal() as session:
        return await create_sweet(session, payload)


# ---------- LIST SWEETS (PUBLIC) ----------
@router.get("")
async def get_all_sweets():
    async with AsyncSessionLocal() as session:
        return await list_sweets(session)


# ---------- SEARCH SWEETS (PUBLIC) ----------
@router.get("/search")
async def search_sweets_endpoint(
    name: str | None = None,
    category: str | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
):
    async with AsyncSessionLocal() as session:
        return await search_sweets(
            session,
            name=name,
            category=category,
            min_price=min_price,
            max_price=max_price,
        )


# ---------- UPDATE SWEET (ADMIN ONLY) ----------
@router.put("/{sweet_id}")
async def update_sweet_endpoint(
    sweet_id: int,
    payload: dict,
    user: User = Depends(require_admin),
):
    async with AsyncSessionLocal() as session:
        sweet = await get_sweet_by_id(session, sweet_id)
        if not sweet:
            raise HTTPException(status_code=404)

        for k, v in payload.items():
            setattr(sweet, k, v)

        await session.commit()
        await session.refresh(sweet)
        return sweet


# ---------- DELETE SWEET (ADMIN ONLY) ----------
@router.delete("/{sweet_id}", status_code=204)
async def delete_sweet_endpoint(
    sweet_id: int,
    user: User = Depends(require_admin),
):
    async with AsyncSessionLocal() as session:
        sweet = await get_sweet_by_id(session, sweet_id)
        if not sweet:
            raise HTTPException(status_code=404)

        await session.delete(sweet)
        await session.commit()
