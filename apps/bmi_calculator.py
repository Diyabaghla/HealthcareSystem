import streamlit as st

# st.set_page_config(page_title="🏥 BMI & Health Risk Assessment", page_icon="⚖️")

st.title("🏥 BMI & Health Risk Assessment")
st.markdown("Calculate your **Body Mass Index** and get health recommendations.")

# User inputs
height = st.number_input("Enter your height (cm):", min_value=100.0, max_value=250.0, step=1.0)
weight = st.number_input("Enter your weight (kg):", min_value=20.0, max_value=200.0, step=0.5)
age = st.number_input("Enter your age:", min_value=5, max_value=120, step=1)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])

if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        bmi = weight / ((height / 100) ** 2)

        # Determine category
        if bmi < 18.5:
            category = "Underweight"
            advice = "Increase calorie intake with healthy foods."
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
            advice = "Maintain your balanced diet and activity."
        elif 25 <= bmi < 29.9:
            category = "Overweight"
            advice = "Incorporate more physical activity and monitor diet."
        else:
            category = "Obese"
            advice = "Consult a healthcare provider for a weight management plan."

        # Display results
        st.subheader(f"Your BMI: **{bmi:.2f}**")
        st.info(f"**Category:** {category}")
        st.markdown(f"💡 **Recommendation:** {advice}")

        # Risk assessment based on BMI & age
        if bmi >= 25:
            if age > 40:
                st.warning("⚠ Higher risk for cardiovascular diseases. Regular check-ups advised.")
            else:
                st.warning("⚠ Monitor your health closely and stay active.")

    else:
        st.error("Please enter valid height and weight.")

st.markdown("---")
st.caption("BMI is a general guide and may not reflect body fat percentage or muscle mass.")

