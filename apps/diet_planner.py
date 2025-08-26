import streamlit as st

# st.set_page_config(page_title="🥗 Diet Planner", layout="centered")
st.title("🥗 Personalized Diet Planner")

st.markdown("Get a healthy diet plan based on your goals.")

goal = st.selectbox("Your Goal", ["Lose Weight", "Gain Muscle", "Maintain Weight"])
diet_type = st.selectbox("Diet Type", ["Vegetarian", "Non-Vegetarian", "Vegan"])

if st.button("Generate Plan"):
    if goal == "Lose Weight":
        st.write("✅ Breakfast: Oats with fruits\n✅ Lunch: Grilled veggies\n✅ Dinner: Soup and salad")
    elif goal == "Gain Muscle":
        st.write("✅ Breakfast: Eggs & toast\n✅ Lunch: Chicken with quinoa\n✅ Dinner: Lentils and rice")
    else:
        st.write("✅ Breakfast: Smoothie\n✅ Lunch: Veggie wrap\n✅ Dinner: Stir-fried tofu & vegetables")
