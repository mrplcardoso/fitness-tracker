from dataclasses import dataclass

@dataclass(slots=True)
class MealItemDTO:

    food_id: int
    food_name: str
    grams: float