from src.dto.meal_item_dto import MealItemDTO


class MealBuilder:

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
            MealItemDTO(food_id=food.id, food_name=food.name, grams=grams))

    def remove_food(self, index: int) -> None:
        self.state.meal_items.pop(index)

    def clear(self) -> None:
        self.state.meal_items.clear()