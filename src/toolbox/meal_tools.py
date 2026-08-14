from src.dto.meal_summary import MealSummary
from src.models.meal_item import MealItem

def calculate(meal_items: MealItem, foods) -> MealSummary:

    summary = MealSummary()
    for item in meal_items:
        
        food = foods[item.food_id]
        factor = item.grams / food.serving

        summary.calories += food.calories * factor
        summary.carbohydrates += food.carbohydrates * factor
        summary.protein += food.protein * factor
        summary.fat += food.fat * factor

    return summary