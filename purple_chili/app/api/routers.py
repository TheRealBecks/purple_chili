from fastapi import APIRouter

from app.api.routes import hero

api_router = APIRouter()
api_router.include_router(hero.router, prefix="/heroes", tags=["heroes"])
