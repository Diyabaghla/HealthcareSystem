import streamlit as st
import google.generativeai as genai
from fpdf import FPDF
from datetime import datetime
import os


# Configure Google Gemini API
genai.configure(api_key="your-API-key")  # Replace with your actual API key

generation_config = {
    "temperature": 0.7,
    "top_p": 0.9,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

def generate_response(input_text):
    response = model.generate_content([
        "You are a medical assistant chatbot. Based on the user's symptoms or queries, predict the possible disease (if any), suggest suitable medications (common OTC or prescription if appropriate), list relevant precautions, recommend suitable workouts (if applicable), and mention the type of doctor/specialist to consult. Always recommend users to see a doctor before acting on your advice.",
        f"User Input: {input_text}",
        "Output:"
    ])
    return response.text.strip()

def generate_diagnosis_pdf(summary_text):
    from fpdf import FPDF
    from datetime import datetime
    import os

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, summary_text)

    filename = f"diagnosis_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    filepath = os.path.join(os.getcwd(), filename)  # Save in current working directory
    pdf.output(filepath)
    return filepath


# Streamlit UI

st.title("💬 AI Medical Chatbot")
st.markdown("Ask health-related questions to get suggestions, workouts, and medicine.")

# Custom Styling
st.markdown("""
    <style>
        .stApp {
            background-color: #f1f8ff;
        }
        .chat-container {
            max-width: 800px;
            margin: auto;
            display: flex;
            flex-direction: column;
            min-height: 65vh;
            overflow-y: auto;
            padding-bottom: 90px;
        }
        .user-message, .bot-message {
            padding: 10px;
            margin: 8px 0;
            border-radius: 10px;
            max-width: fit-content;
            word-wrap: break-word;
        }
        .user-message {
            background-color: #cce5ff;
            align-self: flex-end;
            text-align: right;
        }
        .bot-message {
            background-color: #e2f0cb;
            align-self: flex-start;
        }
        .title {
            font-size: 2rem;
            font-weight: bold;
            color: #007acc;
            text-align: center;
            margin-bottom: 10px;
        }
        .input-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: fixed;
            bottom: 10px;
            width: 100%;
            max-width: 800px;
            left: 50%;
            transform: translateX(-50%);
            background-color: white;
            padding: 10px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
        }
        .input-container input {
            flex-grow: 1;
            padding: 10px;
            font-size: 1.1rem;
            border: none;
            outline: none;
            border-radius: 5px;
        }
        .input-container button {
            margin-left: 10px;
            padding: 10px 15px;
            font-size: 1rem;
            border: none;
            border-radius: 5px;
            background-color: #007acc;
            color: white;
            cursor: pointer;
        }
        .input-container button:hover {
            background-color: #005c99;
        }
    </style>
""", unsafe_allow_html=True)

# Page Title
# st.markdown("""
#     <div class='title'>
#         🩺 <span style='color: #333;'>Your Healthcare Assistant</span>
#     </div>
# """, unsafe_allow_html=True)

# Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

chat_container = st.container()

with chat_container:
    st.markdown("<div class='chat-container' id='chat-box'>", unsafe_allow_html=True)
    for message in st.session_state.chat_history:
        role_class = "user-message" if message["role"] == "user" else "bot-message"
        st.markdown(f"<div class='{role_class}'>{message['content']}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# JavaScript for Auto-Scroll
st.markdown("""
    <script>
    function scrollToBottom() {
        var chatBox = document.getElementById("chat-box");
        chatBox.scrollTop = chatBox.scrollHeight;
    }
    setTimeout(scrollToBottom, 100);
    </script>
""", unsafe_allow_html=True)

# User Input
user_input = st.chat_input("Describe your symptoms or ask a health question...")
if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with chat_container:
        st.markdown(f"<div class='user-message'>{user_input}</div>", unsafe_allow_html=True)

    # Generate bot response
    bot_response = generate_response(user_input)
    st.session_state.chat_history.append({"role": "assistant", "content": bot_response})
    with chat_container:
        st.markdown(f"<div class='bot-message'>{bot_response}</div>", unsafe_allow_html=True)

        pdf_path = generate_diagnosis_pdf(bot_response)

        with chat_container:
            with open(pdf_path, "rb") as f:
                st.download_button(
                    label="📄 Download Diagnosis Summary",
                    data=f,
                    file_name=os.path.basename(pdf_path),
                    mime="application/pdf"
                )

