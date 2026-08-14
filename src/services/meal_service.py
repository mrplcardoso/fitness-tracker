from datetime import date
from src.models.meal import Meal
from src.repositories.meal_repository import MealRepository
from src.dto.meal_dto import MealDTO
from src.models.meal_item import MealItem
from src.dto.meal_item_dto import MealItemDTO

class MealService:
    
    def __init__(self, repository: MealRepository):
        self.repository = repository
        
    def add_meal(self, date: date, name: str, items: list[MealItem]) -> None:
        meal = Meal(date=date, name=name, items=items)
        self.repository.add(meal)

    def save(self, dto: MealDTO) -> Meal:
        meal = Meal(date=dto.date, name=dto.name)

        meal.items = [MealItem(food_id=item.food_id, grams=item.grams)
                                for item in dto.items]

        return self.repository.save(meal)

    def get_by_date(self, meal_date: date) -> list[MealDTO]:
        meals = self.repository.find_by_date(meal_date)
        selected = [MealDTO(id=meal.id, date=meal.date, name=meal.name,
                    items=[MealItemDTO(food_id=item.food.id, food_name=item.food.name, grams=item.grams,
                                        calories=item.food.calories, carbohydrates=item.food.carbohydrates, 
                                        protein=item.food.protein,
                                        fat=item.food.fat) for item in meal.items]
                    ) for meal in meals]
        return selected