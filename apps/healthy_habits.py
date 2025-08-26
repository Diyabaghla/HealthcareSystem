import streamlit as st
import datetime

# st.set_page_config(page_title="🍏 Healthy Habits", layout="centered")
st.title("🍏 Healthy Habits Tracker")

st.markdown("Track and improve your daily health habits.")

# Water intake
st.subheader("💧 Water Intake")
water_glasses = st.slider("Glasses of water today", 0, 20, 8)
if water_glasses >= 8:
    st.success("Great job! You met your daily goal.")
else:
    st.warning("Try to drink at least 8 glasses daily.")

# Exercise
st.subheader("🏃 Exercise Tracker")
exercise_minutes = st.slider("Minutes exercised today", 0, 120, 30)
if exercise_minutes >= 30:
    st.success("Well done! Exercise goal met.")
else:
    st.info("Try to get at least 30 minutes daily.")

# Sleep
st.subheader("🛏️ Sleep Tracker")
sleep_hours = st.slider("Hours slept last night", 0, 12, 7)
if sleep_hours >= 7:
    st.success("Perfect! Enough sleep.")
else:
    st.warning("Aim for 7+ hours daily.")
# Healthy Eating Tip
st.subheader("🥗 Healthy Eating Tip")
healthy_tips = [
    "Eat more vegetables and fruits.",
    "Avoid sugary drinks.",
    "Include protein in every meal.",
    "Limit processed food."
]
st.info(healthy_tips[datetime.datetime.now().day % len(healthy_tips)])
# Daily tip
tips = [
    "Start your day with a glass of warm water.",
    "Take a 10-minute walk after lunch.",
    "Avoid screens 1 hour before bed.",
    "Eat at least 2 servings of vegetables daily."
]
st.info(f"💡 {tips[datetime.datetime.now().day % len(tips)]}")

