from src.builders.meal_builder import MealBuilder
from src.dto.meal_dto import MealDTO
from src.repositories.food_repository import FoodRepository
from src.services.meal_service import MealService


class MealViewModel:

    def __init__(self, session_state):
        self.foods = FoodRepository().get_all()
        self.food_map = { food.id: food for food in self.foods }
        self.builder = MealBuilder(session_state, self.food_map)
        self.meal_service = MealService()

    @property
    def summary(self):
        return self.builder.summary

    @property
    def items(self):
        return self.builder.items

    @property
    def is_empty(self):
        return self.builder.is_empty

    def add_food(self, food, grams):
        self.builder.add_food(food, grams)

    def remove_food(self, index):
        self.builder.remove_food(index)

    def clear(self):
        self.builder.clear()

    def save(self, meal_date, meal_name):
        dto = MealDTO(date=meal_date, name=meal_name,
                      items=self.builder.items.copy())

        self.meal_service.save(dto)
        self.builder.clear()