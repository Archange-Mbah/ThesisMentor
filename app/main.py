from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.router import router

app = FastAPI(title="ThesisMentor")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(router)
