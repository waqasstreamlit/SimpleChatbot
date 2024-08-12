import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the API key
google_api_key = st.secrets["Google_Api_key"]
genai.configure(api_key=google_api_key)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to get response from the model
def get_chatbot_response(user_input):
    try:
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return "Sorry, something went wrong."

# Streamlit interface
st.set_page_config(page_title="Simple Chatbot", layout="centered")

# Title Section
st.markdown("""
    <div style="
        background-color: #FF8033;
        color: white;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
    ">
        <h1>🤖 Simple Chatbot by Waqas 🤖</h1>
        
    </div>
    """, unsafe_allow_html=True)
st.write("Powered by Google Generative AI")

# Write Area Section
# st.markdown("""
#     <div style="
#         background-color: #33FFE3;
#         border-radius: 12px;
#         padding: 20px;
#         margin: 20px 0;
#         box-shadow: 0 4px 8px rgba(0,0,0,0.1);
#     ">
#         <p>Powered by Google Generative AI</p>
#      </div>
#     """, unsafe_allow_html=True)

# Initialize chat history if not present
if "history" not in st.session_state:
    st.session_state["history"] = []

# Display chat history
for user_message, bot_message in st.session_state.history:
    st.markdown(f"""
    <div style="
        background-color: #ffffff;
        border-radius: 12px;
        padding: 12px 18px;
        margin: 8px 0;
        max-width: 75%;
        text-align: left;
        display: inline-block;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    ">
        <p style="margin: 0; font-size: 16px; color: #333;"><b>You:</b> {user_message}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="
        background-color: #e6ffe6;
        border-radius: 12px;
        padding: 12px 18px;
        margin: 8px 0;
        max-width: 75%;
        text-align: left;
        display: inline-block;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    ">
        <p style="margin: 0; font-size: 16px; color: #333;"><b>Bot:</b> {bot_message}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# # Form Section
# st.markdown("""
#     <div style="
#         background-color: #e8f0fe;
#         border-radius: 12px;
#         padding: 20px;
#         margin-top: 20px;
#         box-shadow: 0 4px 8px rgba(0,0,0,0.1);
#     ">
#     """, unsafe_allow_html=True)

# Streamlit form for user input
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("", max_chars=200)
    submit_bt = st.form_submit_button("Send")

    if submit_bt:
        if user_input:
            response = get_chatbot_response(user_input)
            st.session_state.history.append((user_input, response))
            st.write(f"**Bot:** {response}")
        else:
            st.warning("Please enter your query.")

st.markdown("</div>", unsafe_allow_html=True)
