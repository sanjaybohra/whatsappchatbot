import streamlit as st

def load_css():
    st.markdown(
        """
        <style>
        .stChatMessage.user {
            background-color: #DCF8C6;
            border-radius: 10px;
            padding: 10px;
        }
        .stChatMessage.assistant {
            background-color: #FFFFFF;
            border-radius: 10px;
            padding: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
