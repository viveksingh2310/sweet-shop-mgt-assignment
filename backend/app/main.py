from fastapi import FastAPI
from app.users.router import router as user_router
# app=FastAPI()
app = FastAPI(
    title="Sweet Management API",
    description="A basic API for Sweet Management",
    version="0.1.0",
)
@app.get("/")
def getHandling():
    return {"message":"The api is working correctly"}
app.include_router(user_router)