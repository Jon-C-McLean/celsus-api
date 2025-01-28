import os

from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from motor.motor_asyncio import AsyncIOMotorClient

CONNECTION_STRING = os.environ['MONGODB_URI']
# client = AsyncIOMotorClient(CONNECTION_STRING)

async def db_lifespan(app: FastAPI):
    app.mongodb_client = AsyncIOMotorClient(CONNECTION_STRING)
    app.database = app.mongodb_client["test"]
    
    ping_response = await app.database.command("ping")
    
    if int(ping_response["ok"]) != 1:
        raise Exception("Cannot connect to MongoDB")
    
    yield
    
    app.mongodb_client.close()

app = FastAPI(lifespan=db_lifespan)

@app.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(url="/docs")

@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}

@app.get("/time", tags=["health"])
def get_current_time():
    return {"time": datetime.now().isoformat()}