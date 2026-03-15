from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.router import router

app = FastAPI(title="ThesisMentor")

# Mount static folders
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.mount("/uploads", StaticFiles(directory="app/static/uploads"), name="uploads")

# Include main router
app.include_router(router)