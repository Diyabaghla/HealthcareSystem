import streamlit as st

def app():
    st.title("🏥 Welcome to Smart Healthcare Assistant")
    st.markdown("""
        This is an all-in-one health assistant where you can:
        - Predict diseases using symptoms
        - Get medical suggestions via AI chatbot
        - See predictions from different ML models
        - Download diagnosis summaries and find specialists
    """)
