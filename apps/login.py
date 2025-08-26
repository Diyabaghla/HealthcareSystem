import streamlit as st

# st.set_page_config(page_title="🔐 Login", layout="centered")

# If user is already logged in, redirect to homepage
if "username" in st.session_state:
    st.switch_page("pages/home.py")

st.title("🔐 Healthcare Assistant Login")

st.markdown("""
Welcome to the **Healthcare Assistant App**.  
Please log in to continue.
""")

username = st.text_input("Enter your name:")

if st.button("Continue") and username.strip():
    username_clean = username.strip().lower().replace(" ", "_")
    st.session_state.username = username_clean
    st.success(f"Welcome, {username.title()}! Redirecting to the app...")
    st.switch_page("pages/home.py")
