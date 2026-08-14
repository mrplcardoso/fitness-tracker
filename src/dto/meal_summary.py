from dataclasses import dataclass

@dataclass(slots=True)
class MealSummary:
    calories: float = 0
    carbohydrates: float = 0
    proteins: float = 0
    fats: float = 0