from fastapi import FastAPI
from app.users.router import router as auth_router

def create_app() -> FastAPI:
    app = FastAPI(title="Sweet Shop Management API")
    app.include_router(auth_router)
    return app

app = create_app()
