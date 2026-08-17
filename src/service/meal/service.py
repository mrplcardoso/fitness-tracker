from datetime import date
from src.repository.meal.model import Meal, Item
from src.repository.meal.repository import MealRepository
from src.view.meal.builder import MealBuilder
from src.view.meal.display import MealDisplay, ItemDisplay

class MealService:
    
    def __init__(self, repository: MealRepository):
        self.repository = repository
        
    def add_meal(self, date: date, name: str, items: list[Item]) -> None:
        meal = Meal(date=date, name=name, items=items)
        self.repository.add(meal)

    def save(self, builder: MealBuilder) -> Meal:
        meal = Meal(date=builder.date, name=builder.name)
        meal.items = [Item(food_id=item.food_id, grams=item.grams)
                                for item in builder.items]

        return self.repository.save(meal)

    def get_by_date(self, meal_date: date) -> list[MealDisplay]:
        meals = self.repository.find_by_date(meal_date)
        selected = [MealDisplay(id=meal.id, date=meal.date, name=meal.name,
                    items=[ItemDisplay(food_id=item.food.id, food_name=item.food.name, grams=item.grams,
                                        calories=item.food.calories, carbohydrates=item.food.carbohydrates, 
                                        protein=item.food.protein,
                                        fat=item.food.fat) for item in meal.items]
                    ) for meal in meals]
        return selected