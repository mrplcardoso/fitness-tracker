from dataclasses import dataclass
from datetime import date


@dataclass(slots=True)
class MealTotals:

    calories: float = 0
    carbohydrates: float = 0
    proteins: float = 0
    fats: float = 0


@dataclass(slots=True)
class ItemDisplay:

    food_id: int
    food_name: str
    grams: float

    calories: float
    carbohydrates: float
    protein: float
    fat: float


@dataclass(slots=True)
class MealDisplay:

    name: str
    date: date
    items: list[ItemDisplay]
    id: int | None = None

