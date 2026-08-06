from datetime import date
from src.services.meal_service import MealService


class DailyLogViewModel:

    def __init__(self, meal_service: MealService):
        self._meal_service = meal_service

    def meals(self, meal_date: date):
        return self._meal_service.get_by_date(meal_date)