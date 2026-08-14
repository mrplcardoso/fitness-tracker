from datetime import date
import streamlit as st

from src.composition.food_composition import FoodComposition
from src.composition.meal_composition import MealComposition
import src.toolbox.meal_tools as meal_tools

food_composition = FoodComposition()
meal_composition = MealComposition(st.session_state, food_composition.foods)
builder = meal_composition.builder

st.set_page_config(page_title="Meals")
st.title("Meals")


####################
# Meal Information 
####################

st.divider()
st.subheader("Meal Information")

with st.form("meal_info"):
    meal_date = st.date_input("Date", value=date.today())
    meal_name = st.text_input("Meal name", placeholder="Lunch")


####################
# Add Food 
####################

st.divider()
st.subheader("Add food")

selected_food = st.selectbox("Food", food_composition.foods, format_func=lambda f: f.name)
grams = st.number_input("Quantity (g)", 1.0, step=1.0)

if st.button("Add"):
    builder.add_food(selected_food, grams)
    st.rerun()


#####################
# Listing / Removing
#####################

st.divider()
st.subheader("Current meal")

if builder.is_empty:
    st.info("No foods added.")
else:
    for i, item in enumerate(builder.items):
        c1, c2, c3 = st.columns([6,2,1])

        c1.write(item.food_name)
        c2.write(f"{item.grams:.0f} g")
        if c3.button("❌", key=i):
            builder.remove_food(i)
            st.rerun()


##########
# Summary
##########

st.divider()
st.subheader("Meal summary")

if not builder.is_empty:

    totals = meal_tools.calculate(builder.items, food_composition.foods)
    c1, c2 = st.columns(2)

    c1.metric("Calories", f"{totals.calories:.0f} kcal")
    c2.metric("Carbohydrates", f"{totals.carbohydrates:.1f} g")
    c1.metric("Protein", f"{totals.protein:.1f} g")
    c2.metric("Fat", f"{totals.fat:.1f} g")
else:
    st.info("Add foods to calculate the meal.")


###########
# Saving / Clearing
###########

st.divider()
c1, c2 = st.columns(2)

if c1.button("Save meal", use_container_width=True):
    if not meal_name.strip():
        st.warning("Please enter a meal name.")
    elif builder.is_empty:
        st.warning("Please add at least one food.")
    else:
        dto = MealDTO(date=meal_date, name=meal_name, items=self.builder.items.copy())
        self.service.save(dto)
        self.builder.clear()
        st.success("Meal saved!")
        st.rerun()

if c2.button("Clear", use_container_width=True):
    meal_model_view.clear()
    st.rerun()