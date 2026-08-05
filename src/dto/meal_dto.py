from dataclasses import dataclass
from datetime import date

from src.dto.meal_item_dto import MealItemDTO


@dataclass(slots=True)
class MealDTO:

    date: date
    name: str
    items: list[MealItemDTO]