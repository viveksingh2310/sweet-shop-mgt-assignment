from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.users.router import router as auth_router
from app.db.database import init_db
from fastapi import Depends
from app.core.dependencies import get_current_user
from app.sweets.router import router as sweets_router
@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

def create_app() -> FastAPI:
    app = FastAPI(
        title="Sweet Shop Management API",
        lifespan=lifespan,
    )
    app.include_router(auth_router)
    app.include_router(sweets_router)
    return app

app = create_app()
@app.get("/api/protected")
async def protected_route(user=Depends(get_current_user)):
    return {"message": "Access granted"}
