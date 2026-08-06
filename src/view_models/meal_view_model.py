from src.builders.meal_builder import MealBuilder
from src.services.meal_service import MealService
from src.dto.meal_dto import MealDTO


class MealViewModel:

    def __init__(self, service: MealService, builder: MealBuilder):
        self.service = service
        self.builder = builder

    def foods(self):
        return list(self.builder.food_map.values())

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
        dto = MealDTO(date=meal_date, name=meal_name, items=self.builder.items.copy())
        self.service.save(dto)
        self.builder.clear()