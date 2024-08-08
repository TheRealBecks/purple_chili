from sqlmodel import SQLModel, create_engine

# SQLModel will create database tables for the models
import app.models  # noqa: F401 # type: ignore[reportUnusedImports]
from app.core.settings import settings

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)
