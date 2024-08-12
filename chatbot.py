import streamlit as st
import google.generativeai as genai
import os
 
from dotenv import load_dotenv
#configure the API key

load_dotenv()
google_api_key = os.getenv('Google_Api_key')
genai.configure(api_key=google_api_key)

#genai.configure(api_key=google_api_key)

#Inetialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

#function to get responce from model
def get_cahtbot_responce(user_input):
    responce = model.generate_content(user_input)
    return responce.text

#streamlit interface
st.set_page_config(page_title="Simple Chatbot", layout="centered")

st.title("👾 Simple Chatbot by Waqas 👾")
st.write("Powered by Google Generative AI")

if "history" not in st.session_state:
    st.session_state["history"] = []

# Display chat history
for user_message, bot_message in st.session_state.history:
    st.markdown(f"""
    <div style="
        background-color: #d1d3e0;
        border-radius: 15px;
        padding: 10px 15px;
        margin: 5px 0;
        max-width: 70%;
        text-align: left;
        display: inline-block;
    ">
        <p style="margin: 0; font-size: 16px; line-height: 1.5;"><b>You:</b> {user_message} 😊</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="
        background-color: #e1ffc7;
        border-radius: 15px;
        padding: 10px 15px;
        margin: 5px 0;
        max-width: 70%;
        text-align: left;
        display: inline-block;
    ">
        <p style="margin: 0; font-size: 16px; line-height: 1.5;"><b>Bot:</b> {bot_message} 🤖</p>
    </div>
    """, unsafe_allow_html=True)


#user_input = input("Enter your question = ")
#output = get_cahtbot_responce(user_input)
#print(output)

#steamlit interface
with st.form(key="chat_form",clear_on_submit=True):
    user_input = st.text_input("",max_chars=200)
    submit_bt = st.form_submit_button("Send")

    if submit_bt:
        if user_input:
            responce = get_cahtbot_responce(user_input)
            st.session_state.history.append((user_input, responce))
            st.write(responce)
        else:
            st.warning("Please enter your query")
