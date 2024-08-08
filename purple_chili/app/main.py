from fastapi import FastAPI

from app.api.routers import api_router
from app.core.postgres import create_db_and_tables
from app.core.settings import settings

create_db_and_tables()

app = FastAPI()

app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(api_router)
