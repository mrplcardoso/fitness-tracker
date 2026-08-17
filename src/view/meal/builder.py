from datetime import date
from display import ItemDisplay


class MealBuilder:

    id: int | None
    name: str
    date: date

    def __init__(self, session_state):
        self.state = session_state

        if "meal_items" not in self.state:
            self.state.meal_items = []

    @property
    def items(self) -> list:
        return self.state.meal_items

    @property
    def is_empty(self) -> bool:
        return len(self.items) == 0

    def add_food(self, food, grams: float) -> None:
        self.state.meal_items.append(
            ItemDisplay(food_id=food.id, food_name=food.name, grams=grams))

    def remove_food(self, index: int) -> None:
        self.state.meal_items.pop(index)

    def clear(self) -> None:
        self.state.meal_items.clear()