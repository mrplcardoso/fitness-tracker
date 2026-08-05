from src.models.food import Food
from src.repositories.food_repository import FoodRepository


class FoodService:

    def __init__(self):

        self.repository = FoodRepository()

    def add_food(
        self,
        name,
        serving,
        calories,
        carbs,
        protein,
        fat,
    ):

        food = Food(
            name=name,
            serving=serving,
            calories=calories,
            carbs=carbs,
            protein=protein,
            fat=fat,
        )

        self.repository.add(food)

    def get_foods(self):
        return self.repository.get_all()

    def get_food(self, name: str):
        return self.repository.get_by_name(name)

    def get_food_map(self):
        foods = self.repository.get_all()

        return {food.id: food for food in foods}