import os
import streamlit as st
import openai

# Page configuration
st.set_page_config(
    page_title="🤖 AI Chatbot",
    layout="centered"
)

# Title
st.title("🤖 AI-powered Chatbot")

# Load API key from environment or secrets
api_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("openai_api_key")
if not api_key:
    st.error("OpenAI API key not found. Please set OPENAI_API_KEY or add it to Streamlit secrets.")
    st.stop()
openai.api_key = api_key

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# Function to handle user input

def handle_user_input():
    user_msg = st.session_state.user_input
    if not user_msg:
        return
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_msg})
    # Generate assistant reply
    with st.spinner("Thinking..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.messages
            )
            assistant_msg = response.choices[0].message.content
        except Exception as e:
            assistant_msg = f"Error: {e}"
    # Append assistant message
    st.session_state.messages.append({"role": "assistant", "content": assistant_msg})
    # Clear input
    st.session_state.user_input = ""

# Display chat messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Chat input with callback
st.chat_input("Type your message here...", key="user_input", on_submit=handle_user_input)
