# chatbot.py

import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load env
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=groq_api_key)

st.set_page_config(page_title="Groq Chatbot", page_icon="🤖", layout="centered")

# Load external CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title
st.markdown('<div class="chat-title">💬 Ask Me Anything</div>', unsafe_allow_html=True)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]

# Display chat messages
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for msg in st.session_state.messages:
    role = msg["role"]
    content = msg["content"]
    css_class = "user" if role == "user" else "assistant"
    st.markdown(f'<div class="chat-message {css_class}">{content}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Chat input
user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.spinner("Thinking..."):
        try:
            response = client.chat.completions.create(
                model="meta-llama/llama-4-scout-17b-16e-instruct",
                messages=st.session_state.messages,
                temperature=0.7,
            )
            reply = response.choices[0].message.content
            st.session_state.messages.append({"role": "assistant", "content": reply})
            st.rerun()  # ✅ Replaces deprecated st.experimental_rerun()
        except Exception as e:
            st.error(f"Error from Groq API: {e}")

