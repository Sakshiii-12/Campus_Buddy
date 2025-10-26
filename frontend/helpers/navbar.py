# frontend/helpers/navbar.py
import streamlit as st

# Function to render a simple navbar with a title
def render_navbar(title="Campus Buddy"):
    st.markdown(f"<div style='padding:10px 0;'><h2 style='margin:0; color:#006644'>{title}</h2></div>", unsafe_allow_html=True)