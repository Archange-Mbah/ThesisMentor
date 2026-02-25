from fastapi import APIRouter
from app.api.endpoints.web import router as web_router
from .endpoints.documents import router as documents_router

router = APIRouter()
router.include_router(web_router)
router.include_router(documents_router)