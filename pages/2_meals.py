from datetime import date
import streamlit as st

import src.toolbox.meal_tools as meal_tools
from src.shared.food_composition import FoodComposition
from src.shared.meal_composition import MealComposition
from src.view.meal.builder import MealBuilder

food_composition = FoodComposition()
meal_composition = MealComposition()
builder = MealBuilder(st.session_state)

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

selected_food = st.selectbox("Food", food_composition.foods.values(), format_func=lambda f: f.name)
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

    totals = meal_tools.totals(builder.items, food_composition.foods.values())
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
        builder.name = meal_name
        builder.date = meal_date
        meal_composition.service.save(builder)

        builder.clear()
        st.success("Meal saved!")
        st.rerun()

if c2.button("Clear", use_container_width=True):
    builder.clear()
    st.rerun()