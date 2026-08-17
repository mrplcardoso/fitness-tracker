from sqlalchemy import Sequence, select
from src.database import SessionLocal
from .model import Food


class FoodRepository:

    def add(self, food: Food) -> None:
        with SessionLocal() as session:
            session.add(food)
            session.commit()

    def get_all(self) -> Sequence[Food]:
        with SessionLocal() as session:
            statement = select(Food)
            return session.scalars(statement).all()

    def get_by_name(self, name: str) -> (Food | None):
        with SessionLocal() as session:
            stmt = select(Food).where(Food.name == name)
            return session.scalar(stmt)