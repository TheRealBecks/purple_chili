"""FastAPI app."""

import logfire
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.routers import api_router
from app.core.postgres import create_db_and_tables
from app.core.settings import backend_settings

logfire.configure(token=backend_settings.LOGFIRE_TOKEN)
logfire.instrument_psycopg()
logfire.instrument_httpx()
logfire.instrument_sqlalchemy()

create_db_and_tables()

app = FastAPI(debug=backend_settings.DEBUG)
logfire.instrument_fastapi(app)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(api_router)

# This code will be used by the Python debugger
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)  # noqa: S104
