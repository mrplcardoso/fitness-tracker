from datetime import date
import streamlit as st

from src.shared.meal_composition import MealComposition

meal_composition = MealComposition()
meal_service = meal_composition.service

st.set_page_config(page_title="Daily Log")
st.title("Daily Log")

selected_date = st.date_input("Date", value=date.today())
meals = meal_service.get_by_date(selected_date)

if len(meals) == 0:
    st.info("No meals registered.")
else:
    for meal in meals:
        st.subheader(meal.name)
        
        for item in meal.items:
            st.write(f"{item.food_name} ({item.grams:.1f} g)")

            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Calories", f"{item.calories:.1f} kcal")
            col3.metric("Carbs", f"{item.carbohydrates:.1f} g")
            col2.metric("Protein", f"{item.protein:.1f} g")
            col4.metric("Fat", f"{item.fat:.1f} g")