from fastapi import APIRouter, Depends, HTTPException,status
from app.db.database import AsyncSessionLocal
from app.sweets.repository import (
    create_sweet,
    list_sweets,
    search_sweets,
    get_sweet_by_id,
    purchase_sweet, 
    restock_sweet
)
from app.users.models import User
from app.core.dependencies import require_admin,get_current_user
router = APIRouter(prefix="/api/sweets", tags=["Sweets"])


@router.post("", status_code=201)
async def add_sweet(
    payload: dict,
    user: User = Depends(require_admin),
):
    async with AsyncSessionLocal() as session:
        return await create_sweet(session, payload)


@router.get("")
async def get_all_sweets():
    async with AsyncSessionLocal() as session:
        return await list_sweets(session)


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

@router.post("/{sweet_id}/purchase")
async def purchase(
    sweet_id: int,
    payload: dict = {},
    user: User = Depends(get_current_user),
):
    qty = payload.get("quantity", 1)

    async with AsyncSessionLocal() as session:
        try:
            sweet = await purchase_sweet(session, sweet_id, qty)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

        if not sweet:
            raise HTTPException(status_code=404, detail="Sweet not found")

        return sweet
#admin routes only
@router.post("/{sweet_id}/restock")
async def restock_sweet_endpoint(
    sweet_id: int,
    payload: dict,
    admin: User = Depends(require_admin),
):
    qty = payload.get("quantity")

    if not isinstance(qty, int) or qty <= 0:
        raise HTTPException(status_code=400, detail="Invalid quantity")

    async with AsyncSessionLocal() as session:
        sweet = await restock_sweet(session, sweet_id, qty)

        if not sweet:
            raise HTTPException(status_code=404)

        return {
            "message": "Restocked successfully",
            "quantity": sweet.quantity,
        }