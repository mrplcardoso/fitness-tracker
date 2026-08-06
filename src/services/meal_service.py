from datetime import date
from src.models.meal import Meal
from src.repositories.meal_repository import MealRepository
from src.dto.meal_dto import MealDTO
from src.models.meal_item import MealItem

class MealService:
    
    def __init__(self, repository: MealRepository):
        self.repository = repository
        
    def add_meal(self, date, name, items):
        meal = Meal(date=date, name=name, items=items)
        self.repository.add(meal)

    def save(self, dto: MealDTO) -> Meal:
        meal = Meal(date=dto.date, name=dto.name)

        meal.items = [MealItem(food_id=item.food_id, grams=item.grams)
                                for item in dto.items]

        return self.repository.save(meal)

    def get_meals(self):
        return self.repository.get_all()

    def get_by_date(self, meal_date: date) -> list[Meal]:
        return self.repository.find_by_date(meal_date)