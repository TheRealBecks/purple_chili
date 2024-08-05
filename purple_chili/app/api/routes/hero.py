from fastapi import APIRouter
from sqlmodel import Session, select

from app.core.postgres import engine
from app.models.hero import Hero

router = APIRouter()


@router.post("/")
def create_hero(hero: Hero) -> Hero:
    with Session(engine) as session:
        session.add(hero)
        session.commit()
        session.refresh(hero)
        return hero


@router.get("/")
def read_heroes():
    print("ja")
    with Session(engine) as session:
        print("hier")
        print(session.exec(select(Hero)).all())
        print("da")
        return session.exec(select(Hero)).all()