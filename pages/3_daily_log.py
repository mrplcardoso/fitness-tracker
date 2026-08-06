from datetime import date
import streamlit as st

from src.composition.daily_log_composition import DailyLogComposition
from src.view_models.daily_log_view_model import DailyLogViewModel

st.set_page_config(page_title="Daily Log")
st.title("Daily Log")

selected_date = st.date_input("Date", value=date.today())

composition = DailyLogComposition()
view_model = DailyLogViewModel(composition.service)
meals = view_model.meals(selected_date)

if len(meals) == 0:
    st.info("No meals registered.")
else:
    for meal in meals:
        st.subheader(meal.name)
        
        for item in meal.items:
            st.write(f"{item.food.name} ({item.grams:.0f} g)")