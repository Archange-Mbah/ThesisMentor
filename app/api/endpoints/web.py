from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")  # Path to your HTML files

# Home page route
@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Chat page route
@router.get("/chat")
async def chat(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})