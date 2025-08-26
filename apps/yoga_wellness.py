import streamlit as st
import datetime

# st.set_page_config(page_title="🧘 Yoga & Wellness", layout="centered")
st.title("🧘 Yoga & Wellness")

st.markdown("""
Improve your health through **Yoga** and **Meditation**.  
Select a focus and follow guided instructions.
""")

# Yoga focus
yoga_type = st.selectbox(
    "Choose a Yoga Focus:",
    ["Morning Energy Boost", "Stress Relief", "Flexibility Improvement", "Back Pain Relief"]
)

# Recommendations + Media
if yoga_type == "Morning Energy Boost":
    st.video("https://www.youtube.com/watch?v=VaoV1PrYft4")
    st.write("Follow this **Sun Salutation** routine daily for better energy.")
elif yoga_type == "Stress Relief":
    st.video("https://www.youtube.com/watch?v=8VwufJrUhic")
    st.write("Try **Anulom Vilom** breathing for 5 minutes to reduce stress.")
elif yoga_type == "Flexibility Improvement":
    st.video("https://www.youtube.com/watch?v=8VwufJrUhic")
    st.write("Daily stretching helps improve flexibility and posture.")
elif yoga_type == "Back Pain Relief":
    st.video("https://www.youtube.com/watch?v=2VuLBYrgG94")
    st.write("Gentle yoga can help relieve lower back pain.")

# Meditation timer
st.subheader("🕒 Meditation Timer")
meditation_minutes = st.slider("Set Meditation Time (minutes)", 1, 30, 5)
if st.button("Start Meditation"):
    st.success(f"🧘 Start meditating for {meditation_minutes} minutes.")

# Progress tracker
st.subheader("📅 My Yoga Progress")
days_practiced = st.number_input("Days practiced this month", 0, 31, 0)
if days_practiced >= 20:
    st.success("Amazing! You’re consistent and committed.")
elif days_practiced >= 10:
    st.info("Good progress, keep it up!")
else:
    st.warning("Try to practice more regularly.")
# Daily Wellness Tip
st.subheader("💡 Daily Wellness Tip")
tips = [
    "Drink 2-3 liters of water daily.",
    "Take deep breaths every hour.",
    "Stretch your body every morning.",
    "Get at least 7 hours of sleep."
]
st.info(tips[datetime.datetime.now().day % len(tips)])
