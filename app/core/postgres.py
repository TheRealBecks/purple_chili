"""Set up Postgres database."""

from sqlmodel import SQLModel, create_engine

# SQLModel will create database tables for the models
import app.models  # noqa: F401 # type: ignore[reportUnusedImports]
from app.core.settings import backend_settings

engine = create_engine(str(backend_settings.SQLALCHEMY_DATABASE_URI))


def create_db_and_tables() -> None:
    """Create database and tables if not exist."""
    SQLModel.metadata.create_all(engine)
