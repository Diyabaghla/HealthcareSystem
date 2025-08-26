import streamlit as st
import random
#
# st.set_page_config(page_title="🧠 Mental Wellness", layout="centered")
st.title("🧠 Mental Wellness")

st.markdown("""
Your mental health matters.  
Take a moment to relax, breathe, and reflect.
""")

# Mood tracker
mood = st.radio("How are you feeling today?", ["😊 Happy", "😌 Calm", "😔 Sad", "😤 Stressed"])
if mood:
    st.write(f"Noted your mood: {mood}")

# Guided relaxation
st.subheader("🌿 Guided Relaxation")
if st.button("Play Relaxing Music"):
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# Positive affirmations
affirmations = [
    "You are stronger than you think.",
    "Every day is a fresh start.",
    "Your potential is limitless.",
    "You deserve to be happy."
]
if st.button("Show Me an Affirmation"):
    st.success(random.choice(affirmations))
