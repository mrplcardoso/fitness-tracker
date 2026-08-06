from src.repositories.food_repository import FoodRepository
from src.services.food_service import FoodService


class FoodComposition:

    def __init__(self):
        self._repository = FoodRepository()
        self._foods = { food.id: food for food in self._repository.get_all() }
        self._service = FoodService(self._repository)

    @property
    def repository(self):
        return self._repository

    @property
    def service(self):
        return self._service

    @property
    def foods(self):
        return self._foods