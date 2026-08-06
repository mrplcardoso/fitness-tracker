from dataclasses import dataclass

@dataclass(slots=True)
class MealSummaryDTO:

    calories: float = 0
    carbohydrates: float = 0
    protein: float = 0
    fat: float = 0