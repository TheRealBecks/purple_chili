"""Example routes for Hero model."""

from collections.abc import Sequence

from fastapi import APIRouter
from sqlmodel import Session, select

from app.core.postgres import engine
from app.core.templates import jinja
from app.models.hero import Hero

router = APIRouter()


@router.post("/")
@jinja.hx("hero/list.html.j2")
def create_hero(hero: Hero) -> Hero:
    """Create a new Hero."""
    with Session(engine) as session:
        session.add(hero)
        session.commit()
        session.refresh(hero)
        return hero


@router.get("/")
@jinja.page("hero/list.html.j2")
def read_heroes() -> Sequence[Hero]:
    """Read all Heroes."""
    with Session(engine) as session:
        return session.exec(select(Hero)).all()
