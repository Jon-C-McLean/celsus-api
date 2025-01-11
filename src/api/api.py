from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(url="/docs")

@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}

@app.get("/time", tags=["health"])
def get_current_time():
    return {"time": datetime.now().isoformat()}