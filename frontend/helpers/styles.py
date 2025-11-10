# frontend/helpers/styles.py
# Shared CSS styling for Campus Buddy (Student + Admin portals)

import streamlit as st

def load_custom_css():
    # Inject consistent design system across both portals.
    st.markdown("""
        <style>
        /* Global Page Styling */
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #f5f7fa 0%, #e4ecf2 100%);
            color: #1e1e1e;
        }

        h1, h2, h3, h4, h5 {
            color: #1b263b;
            font-weight: 600;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #2b2f3a !important;
            color: white !important;
        }

        [data-testid="stSidebar"] * {
            color: #f1f1f1 !important;
        }

        /* Sidebar Buttons / Radio / Logout */
        .stRadio > label, .stSidebar .stButton > button {
            font-weight: 500 !important;
        }

        section[data-testid="stSidebar"] .stButton>button {
            background-color: #457b9d !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 0.5em 1em !important;
            transition: all 0.3s ease;
        }
        section[data-testid="stSidebar"] .stButton>button:hover {
            background-color: #1d3557 !important;
        }

        /* Buttons */
        div.stButton > button {
            background-color: #1d3557;
            color: white;
            border-radius: 8px;
            padding: 0.6em 1.2em;
            border: none;
            transition: all 0.3s ease;
            font-weight: 500;
        }
        div.stButton > button:hover {
            background-color: #457b9d;
            transform: scale(1.02);
        }

        /* Inputs */
        .stTextInput>div>div>input, textarea {
            border-radius: 6px !important;
            border: 1px solid #ccc !important;
            padding: 0.4em !important;
        }

        /* Info + Alerts */
        .stAlert {
            border-radius: 10px;
            padding: 1em;
        }

        /* Navbar Header */
        .navbar {
            background-color: #1d3557;
            color: white;
            padding: 0.8em 1.5em;
            border-radius: 8px;
            margin-bottom: 1.2em;
        }
        .navbar h2 {
            color: white;
            font-size: 1.4em;
            margin: 0;
        }

        /* Expanders */
        div[data-testid="stExpander"] {
            border-radius: 8px;
            border: 1px solid #ccc;
            background-color: white;
        }
        .streamlit-expanderHeader {
            font-weight: 600;
            background-color: #f1f3f8;
            border-radius: 6px;
            padding: 0.5em;
        }

        /* Data Table */
        .stDataFrame {
            border-radius: 8px;
            overflow: hidden;
        }

        /* Download Button */
        div[data-testid="stDownloadButton"] > button {
            background-color: #457b9d !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 0.6em 1.2em !important;
            font-weight: 500;
        }
        div[data-testid="stDownloadButton"] > button:hover {
            background-color: #1d3557 !important;
        }

        /* Hide Streamlit Footer */
        footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)


def render_navbar(title: str):
    # Top bar with consistent theme.
    st.markdown(f"""
        <div class="navbar">
            <h2>{title}</h2>
        </div>
    """, unsafe_allow_html=True)
