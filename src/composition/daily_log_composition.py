from src.repositories.meal_repository import MealRepository
from src.services.meal_service import MealService


class DailyLogComposition:

    def __init__(self):
        repository = MealRepository()
        self._service = MealService(repository)

    @property
    def service(self):
        return self._service