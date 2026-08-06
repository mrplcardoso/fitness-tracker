from datetime import date
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from src.database import SessionLocal
from src.models.meal import Meal
from src.models.meal_item import MealItem


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
                         .options(joinedload(Meal.items).joinedload(MealItem.food))
                         .where(Meal.date == meal_date))

            return (session.execute(statement).unique().scalars().all())

    def delete(self, meal_id: int):
        with SessionLocal() as session:
            meal = session.get(Meal, meal_id)
            if meal is None:
                return

            session.delete(meal)
            session.commit()