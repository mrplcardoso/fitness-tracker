from src.repository.food.model import Food
from src.repository.meal.model import Item
from src.view.meal.display import MealTotals

def totals(items: list[Item], foods: list[Food]) -> MealTotals:
    totals = MealTotals()

    for item in items:
        food = foods[item.food_id]
        factor = item.grams / food.serving

        totals.calories += food.calories * factor
        totals.carbohydrates += food.carbohydrates * factor
        totals.protein += food.protein * factor
        totals.fat += food.fat * factor

    return totals