from src.dto.meal_summary_dto import MealSummaryDTO


class MealCalculator:

    def calculate(self, meal_items, foods):
        summary = MealSummaryDTO()

        for item in meal_items:
            food = foods[item.food_id]

            factor = item.grams / food.serving

            summary.calories += food.calories * factor
            summary.carbohydrates += food.carbohydrates * factor
            summary.protein += food.protein * factor
            summary.fat += food.fat * factor

        return summary