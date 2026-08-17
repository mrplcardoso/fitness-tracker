from datetime import date
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from src.database import SessionLocal
from .model import Meal
from .model import Item


class MealRepository:

    def save(self, meal: Meal) -> Meal:
        with SessionLocal() as session:
            session.add(meal)
            session.commit()
            session.refresh(meal)
            return meal
    
    def find_by_date(self, meal_date: date) -> list[Meal]:
        with SessionLocal() as session:
            statement = (select(Meal)
                         .options(joinedload(Meal.items).joinedload(Item.food))
                         .where(Meal.date == meal_date))

            return (session.execute(statement).unique().scalars().all())

    def delete(self, meal_id: int) -> None:
        with SessionLocal() as session:
            meal = session.get(Meal, meal_id)
            if meal is None:
                return

            session.delete(meal)
            session.commit()