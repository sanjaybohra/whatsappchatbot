import streamlit as st
from chatbot.ui.sidebar import render_sidebar
from chatbot.ui.chat_ui import render_chat_ui
from chatbot.ui.styles import load_css

st.set_page_config(page_title="WhatsApp AI Bot", layout="wide")

load_css()
render_sidebar()
render_chat_ui()
