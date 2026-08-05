import pandas as pd
import streamlit as st
from src.services.food_service import FoodService

service = FoodService()

st.title("Fitness Tracker")
st.header("Food Register")

name = st.text_input("Name")
serving = st.number_input(
    "Reference serving (g)",
    value=100.0,
)
calories = st.number_input("Calories")
carbs = st.number_input("Carbohydrates")
protein = st.number_input("Proteins")
fat = st.number_input("Fats")

if st.button("Save"):

    service.add_food(
        name,
        serving,
        calories,
        protein,
        carbs,
        fat,
    )

    st.success("Food saved.")

foods = service.get_foods()
df = pd.DataFrame(
    [
        {
            "Name": f.name,
            "Serving": f.serving,
            "Calories": f.calories,
            "Carbohydrates": f.carbs,
            "Proteins": f.protein,
            "Fats": f.fat,
        }
        for f in foods
    ]
)
st.dataframe(df)