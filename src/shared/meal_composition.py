from src.repository.meal.repository import MealRepository
from src.service.meal.service import MealService

class MealComposition:

    def __init__(self):
        self._repository = MealRepository()
        self._service = MealService(self._repository)

    @property
    def repository(self):
        return self._repository

    @property
    def service(self):
        return self._service