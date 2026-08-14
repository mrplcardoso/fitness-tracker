from src.repositories.meal_repository import MealRepository
from src.services.meal_service import MealService
from src.builders.meal_builder import MealBuilder

class MealComposition:

    def __init__(self, session_state):
        self._repository = MealRepository()
        self._service = MealService(self._repository)
        self._builder = MealBuilder(session_state)

    @property
    def repository(self):
        return self._repository

    @property
    def service(self):
        return self._service

    @property
    def builder(self):
        return self._builder