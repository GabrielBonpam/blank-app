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

# Set OpenAI API key from environment or secrets
api_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("openai_api_key")
if not api_key:
    st.error("OpenAI API key not found. Please set it in the environment variable OPENAI_API_KEY or in Streamlit secrets.")
    st.stop()
openai.api_key = api_key

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# Chat input
user_input = st.chat_input("Type your message here...")
if user_input:
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    # Display user message
    st.chat_message("user").write(user_input)

    # Call OpenAI Chat API
    with st.spinner("Thinking..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.messages
            )
            assistant_msg = response.choices[0].message.content
            st.session_state.messages.append({"role": "assistant", "content": assistant_msg})
            # Display assistant message
            st.chat_message("assistant").write(assistant_msg)
        except Exception as e:
            st.error(f"Error: {e}")

# Display previous messages on page load
for msg in st.session_state.messages[1:]:  # skip system
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    elif msg["role"] == "assistant":
        st.chat_message("assistant").write(msg["content"])
