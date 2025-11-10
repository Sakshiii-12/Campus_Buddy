# frontend/app.py
# Campus Buddy Student Portal
import streamlit as st
import os, sys
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Imports
from backend.database import init_db, add_complaint, get_complaints_by_email
from backend.auth import validate_student_login
from backend.config import general_categories, critical_categories
from backend.chatbot import get_chatbot_response
from frontend.helpers.styles import load_custom_css

# PAGE CONFIG 
st.set_page_config(page_title="Campus Buddy - Student", layout="wide", page_icon="🎓")
init_db()
load_custom_css()

# SESSION STATE
if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "email" not in st.session_state: st.session_state.email = None
if "chat_history" not in st.session_state: st.session_state.chat_history = []

# NAVBAR 
def render_navbar(title="Campus Buddy"):
    st.markdown(f"""
        <div class="navbar">
            <h2>{title}</h2>
        </div>
    """, unsafe_allow_html=True)

# LOGIN PAGE
if not st.session_state.logged_in:
    render_navbar("Welcome to Campus Buddy")
    st.title("Student Login")
    email = st.text_input("Email", placeholder="Enter your college email")
    password = st.text_input("Password", type="password", placeholder="Enter your password")

    if st.button("Login"):
        if validate_student_login(email, password):
            st.session_state.logged_in = True
            st.session_state.email = email
            st.success("Login successful! Redirecting...")
            st.rerun()
        else:
            st.error("Invalid credentials. Please try again.")
    st.stop()

# SIDEBAR
st.sidebar.title("Campus Buddy")
page = st.sidebar.radio("Navigate", ["Home", "Register Complaint", "My Complaints", "Chatbot"])
if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.session_state.email = None
    st.rerun()

# HOME
if page == "Home":
    render_navbar("Welcome to Campus Buddy 🎓")
    st.markdown("""
    Campus Buddy allows students to:
    - Register complaints regarding academics, infrastructure, hostel, and more.
    - Track the progress of your complaints in real time.
    - Chat with a virtual assistant for quick help and guidance.
    - Get tips, FAQs, and campus service guidance.
    - Stay informed and ensure your concerns are addressed efficiently.
    """)
    img_path = "frontend/helpers/assets/campus_buddy_home.png"
    if os.path.exists(img_path):
        st.image(img_path, caption="Campus Buddy Support", use_column_width=True)

# REGISTER COMPLAINT 
elif page == "Register Complaint":
    render_navbar("Register a Complaint")
    st.subheader("Complaint Form")

    complaint_type = st.selectbox("Complaint Type", ["General", "Critical"])
    if complaint_type == "General":
        category = st.selectbox("Select Category", list(general_categories.keys()))
        st.caption(f"Examples: {general_categories[category]}")
    else:
        category = st.selectbox("Select Category", list(critical_categories.keys()))
        st.caption(f"Examples: {critical_categories[category]}")

    description = st.text_area("Describe your complaint")
    is_anonymous = st.checkbox("Submit anonymously")
    file_upload = st.file_uploader("Attach a file (optional)", type=["jpg","png","pdf","jpeg"])

    if st.button("Submit Complaint"):
        file_path = None
        if file_upload:
            uploads_dir = "uploads"
            os.makedirs(uploads_dir, exist_ok=True)
            file_path = os.path.join(uploads_dir, file_upload.name)
            with open(file_path, "wb") as f:
                f.write(file_upload.getbuffer())

        if not description:
            st.warning("Please enter a description for your complaint.")
        else:
            add_complaint(complaint_type, category, None, description, is_anonymous, file_path, st.session_state.email)
            st.success("Complaint submitted successfully!")

# MY COMPLAINTS
elif page == "My Complaints":
    render_navbar("My Complaints")
    email = st.session_state.email
    st.markdown(f"### Logged in as: {email}")

    complaints = get_complaints_by_email(email)
    if not complaints:
        st.info("No complaints found for this email.")
    else:
        for row in complaints:
            (
                cid, ctype, cat, _, desc, anon, file_path,
                email, status, assigned, created
            ) = row

            # Background color based on status
            bg_color = "#d4edda" if status == "Resolved" else "#fff3cd" if status == "In Progress" else "#f8d7da"
            text_color = "#155724" if status == "Resolved" else "#856404" if status == "In Progress" else "#721c24"

            assigned_text = assigned if assigned else "Not yet assigned"

            # Build HTML content separately for clarity
            html_content = f"""
                <div style="
                    background-color:{bg_color};
                    color:{text_color};
                    border-radius:10px;
                    padding:10px;
                    margin-bottom:10px;
                    border:1px solid {text_color};
                ">
                    <strong>ID {cid} — {ctype}</strong><br>
                    <strong>Category:</strong> {cat}<br>
                    <strong>Description:</strong> {desc}<br>
                    <strong>Submitted:</strong> {created}<br>
                    <strong>Assigned to:</strong> {assigned_text}<br>
            """

            if file_path:
                html_content += f"<strong>Attachment:</strong> {file_path}<br>"

            if anon:
                html_content += "<em>Submitted anonymously</em><br>"

            html_content += f"<strong>Status:</strong> {status}</div>"

            # Render the formatted HTML
            st.markdown(html_content, unsafe_allow_html=True)

# CHATBOT
elif page == "Chatbot":
    render_navbar("Campus Buddy Chatbot")
    st.markdown("Ask questions about complaints, campus services, library, hostel, academics, and more.")

    # Display chat history
    for role, msg in st.session_state.chat_history:
        if role == "user":
            st.chat_message("user").markdown(f"**You:** {msg}")
        else:
            st.chat_message("assistant").markdown(msg)

    # Chat input
    if user_input := st.chat_input("Ask Campus Buddy..."):
        # Add user message
        st.session_state.chat_history.append(("user", user_input))

        # Get response and source type
        reply_text, reply_type = get_chatbot_response(user_input)

        # Label based on source
        if reply_type == "rule":
            label = "(Campus Buddy — Instant Answer)"
        elif reply_type == "gemini":
            label = "(Campus Buddy — Smart Assistant)"
        else:
            label = "(Campus Buddy)"

        # Display assistant message with label
        st.session_state.chat_history.append(("assistant", f"{reply_text}\n\n*{label}*"))

        st.rerun()
