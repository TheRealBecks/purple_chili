"""Example models for Hero."""

from sqlmodel import Field, SQLModel  # type: ignore[reportUnknownVariableType]


class Hero(SQLModel, table=True):
    """Example Hero model."""

    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None
