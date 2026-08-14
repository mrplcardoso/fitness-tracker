from sqlalchemy import Sequence

from src.models.food import Food
from src.repositories.food_repository import FoodRepository


class FoodService:

    def __init__(self, repository: FoodRepository):
        self.repository = repository

    def add_food(self, name: str, serving: float, calories: float, carbohydrates: float,
                        protein: float, fat: float) -> None:
        food = Food(name=name, serving=serving, calories=calories,
                    carbohydrates=carbohydrates, protein=protein, fat=fat)

        self.repository.add(food)

    def get_foods(self) -> Sequence[Food]:
        return self.repository.get_all()

    def get_food(self, name: str)  -> (Food | None):
        return self.repository.get_by_name(name)

    def get_food_map(self) -> dict[int, Food]:
        foods = self.get_foods()
        return { food.id: food for food in foods }