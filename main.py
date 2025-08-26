import streamlit as st
import pandas as pd
import os

# ✅ Global page config
st.set_page_config(page_title="Healthcare Assistant App", layout="centered", page_icon="🩺")

# -------------------------
# File to store user data
# -------------------------
USER_DATA_FILE = "users.csv"

# Create file if it doesn't exist
if not os.path.exists(USER_DATA_FILE):
    pd.DataFrame(columns=["email", "password", "name"]).to_csv(USER_DATA_FILE, index=False)

# Load user data
def load_users():
    return pd.read_csv(USER_DATA_FILE)

# Save new user
def save_user(email, password, name):
    df = load_users()
    if email in df["email"].values:
        return False  # User already exists
    new_user = pd.DataFrame([[email, password, name]], columns=["email", "password", "name"])
    df = pd.concat([df, new_user], ignore_index=True)
    df.to_csv(USER_DATA_FILE, index=False)
    return True

# -------------------------
# Login/Signup Logic
# -------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_email = None
    st.session_state.user_name = None

if not st.session_state.logged_in:
    menu = st.radio("Select Option", ["Login", "Sign Up"], horizontal=True)

    if menu == "Login":
        st.title("🔐 Healthcare Assistant Login")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            users = load_users()
            user = users[(users["email"] == email) & (users["password"] == password)]
            if not user.empty:
                st.session_state.logged_in = True
                st.session_state.user_email = email
                st.session_state.user_name = user.iloc[0]["name"]
                st.success(f"✅ Welcome back, {st.session_state.user_name}!")
                st.rerun()
            else:
                st.error("❌ Invalid email or password.")

    elif menu == "Sign Up":
        st.title("📝 Create a New Account")
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")

        if st.button("Sign Up"):
            if password != confirm_password:
                st.error("❌ Passwords do not match.")
            elif save_user(email, password, name):
                st.success("✅ Account created! Please log in.")
            else:
                st.error("❌ Email already exists. Please use another.")

    st.stop()  # 🚫 Stop here until logged in

# -------------------------
# Sidebar Navigation (Only after login)
# -------------------------
st.sidebar.title(f"🩺 Welcome, {st.session_state.user_name}")
app_mode = st.sidebar.selectbox(
    "Select Page",
    [
        "🏠 Home - About the Project",
        "🧪 Disease Prediction",
        "💬 Virtual AI Assistant",
        "👨‍⚕️ Disease & Doctor Recommendation",
        "🧘 Yoga Wellness",
        "🏥 BMI Calculator",
        "🍏 Healthy Habits",
        "🧠 Mental Wellness",
        "🥗 Diet Planner"
    ]
)

# -------------------------
# Pages
# -------------------------
if app_mode == "🏠 Home - About the Project":
    st.title("Healthcare Recommendation System")
    st.markdown(f"""
    ### 🧠 Intelligent Disease Prediction & Health Assistant  
    Welcome **{st.session_state.user_name}**!  

    This system uses AI to:
    - 🔍 Predict diseases from symptoms
    - 👨‍⚕️ Recommend the right specialist
    - 📈 Virtual AI Assistant
    """)

elif app_mode == "🧪 Disease Prediction":
    exec(open("apps/disease_predict.py", encoding="utf-8").read())

elif app_mode == "💬 Virtual AI Assistant":
    exec(open("apps/chatbot.py", encoding="utf-8").read())

elif app_mode == "👨‍⚕️ Disease & Doctor Recommendation":
    exec(open("apps/doctor_spec.py", encoding="utf-8").read())



elif app_mode == "🍏 Healthy Habits":
    exec(open("apps/healthy_habits.py", encoding="utf-8").read())

elif app_mode == "🧘 Yoga Wellness":
    exec(open("apps/yoga_wellness.py", encoding="utf-8").read())
elif app_mode == "🏥 BMI Calculator":
    exec(open("apps/bmi_calculator.py", encoding="utf-8").read())


elif app_mode == "🧠 Mental Wellness":
    exec(open("apps/mental_wellness.py", encoding="utf-8").read())

elif app_mode == "🥗 Diet Planner":
    exec(open("apps/diet_planner.py", encoding="utf-8").read())

