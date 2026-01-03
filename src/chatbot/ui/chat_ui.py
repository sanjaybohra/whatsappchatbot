import streamlit as st
from chatbot.core.chat_engine import get_bot_response


def render_chat_ui():

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Input box (WhatsApp style)
    user_input = st.chat_input("Type a message")

    if user_input:
        # Store user message
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        with st.chat_message("user"):
            st.markdown(user_input)

        # Bot response (streaming)
        with st.chat_message("assistant"):
            placeholder = st.empty()
            full_response = ""

            for token in get_bot_response(user_input):
                full_response += token
                placeholder.markdown(full_response)

        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )
