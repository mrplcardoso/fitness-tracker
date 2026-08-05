from dataclasses import dataclass

@dataclass(slots=True)
class MealSummaryDTO:

    calories: float = 0
    carbs: float = 0
    protein: float = 0
    fat: float = 0