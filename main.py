import streamlit as st
from  chatbot import get_bot_response

st.set_page_config(page_title="Zeru AI", layout="centered")
st.title=("Zeru AI Assistant (Offline - No API key)")

st.markdown("Ask me anything")

user_input = st.text_input("You:")

if user_input:
    with st.spinner("Thinking..."):
        reply = get_bot_response(user_input)
        st.markdown(f"**Bot:** {reply}")