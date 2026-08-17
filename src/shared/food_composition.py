from src.repository.food.model import Food
from src.repository.food.repository import FoodRepository
from src.service.food.service import FoodService


class FoodComposition:

    def __init__(self):
        self._repository = FoodRepository()
        self._service = FoodService(self._repository)
        self._foods = self._service.get_food_map()

    @property
    def repository(self) -> FoodRepository:
        return self._repository

    @property
    def service(self) -> FoodService:
        return self._service

    @property
    def foods(self) -> dict[int, Food]:
        return self._foods