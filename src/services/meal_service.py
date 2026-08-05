from src.models.food import Meal
from src.repositories.meal_repository import MealRepository


class MealService:
    
    def __init__(self):
        self.repository = MealRepository()

    def add_meal(self, date, name, items):
        meal = Meal(date=date, name=name, items=items)
        self.repository.add(meal)

    def get_meals(self):
        return self.repository.get_all()