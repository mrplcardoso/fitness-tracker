from src.calculations.meal_calculator import MealCalculator
from src.dto.meal_item_dto import MealItemDTO


class MealBuilder:

    def __init__(self, session_state, foods_map):

        self.state = session_state
        self.foods_map = foods_map
        self.calculator = MealCalculator()

        if "meal_items" not in self.state:
            self.state.meal_items = []

    @property
    def items(self):
        return self.state.meal_items

    def add_food(self, food, grams):

        self.state.meal_items.append(
            MealItemDTO(
                food_id=food.id,
                food_name=food.name,
                grams=grams,
            )
        )

    def remove_food(self, index):

        self.state.meal_items.pop(index)

    def clear(self):

        self.state.meal_items.clear()

    @property
    def is_empty(self):

        return len(self.items) == 0

    @property
    def summary(self):

        return self.calculator.calculate(
            self.items,
            self.foods_map,
        )