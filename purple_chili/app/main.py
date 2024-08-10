"""FastAPI app."""

import logfire
from fastapi import FastAPI

from app.api.routers import api_router
from app.core.postgres import create_db_and_tables
from app.core.settings import settings

logfire.configure(token=settings.LOGFIRE_TOKEN)
logfire.instrument_psycopg()
logfire.instrument_httpx()
logfire.instrument_sqlalchemy()

create_db_and_tables()

app = FastAPI()
logfire.instrument_fastapi(app)

app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(api_router)
