from fastapi import FastAPI
# app=FastAPI()
app = FastAPI(
    title="Sweet Management API",
    description="A basic API for Sweet Management",
    version="0.1.0",
)
@app.get("/")
def getHandling():
    return {"message":"The api is working correctly"}