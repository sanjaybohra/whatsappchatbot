import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.title("💬 WhatsApp AI")
        st.success("Using Ollama (local)")
        st.markdown("Model: **phi3**")
        st.markdown("---")
        st.info("No API key required")
