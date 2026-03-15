from fastapi import APIRouter
from .endpoints.web import router as web_pages_router
from .endpoints.documents import router as documents_router

router = APIRouter()

# Include specific routers
router.include_router(web_pages_router)
router.include_router(documents_router)