# frontend/app.py
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from datetime import datetime
from backend.database import add_complaint, get_all_complaints, init_db
from backend.nlp_utils import detect_priority
from backend.auth import validate_student_login
from backend.config import general_categories, critical_categories, general_faqs, category_faqs
from frontend.helpers.styles import global_styles
from frontend.helpers.faq_renderer import render_faqs
from frontend.helpers.complaint_handler import handle_edit_complaint, handle_withdraw_complaint

# INIT 
init_db()
st.set_page_config(page_title="Campus Buddy", layout="centered", page_icon="🎓")
st.markdown(global_styles, unsafe_allow_html=True)

# SESSION
if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "email" not in st.session_state: st.session_state.email = ""
if "page" not in st.session_state: st.session_state.page = "Complaint"

# LOGIN
if not st.session_state.logged_in:
    st.markdown('<div class="login-title">Campus Buddy</div>', unsafe_allow_html=True)
    st.markdown('<div class="login-subtitle">Login with your college email</div>', unsafe_allow_html=True)
    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.form_submit_button("Login"):
            if validate_student_login(email, password):
                st.session_state.logged_in = True
                st.session_state.email = email
                st.session_state.page = "Complaint"
                st.stop()  # Immediately stop rendering, page reloads showing the complaint page
            else:
                st.error("Invalid credentials.")
    st.stop()  # Stop execution until login succeeds

# MAIN APP (ONLY AFTER LOGIN
st.sidebar.markdown(
    f"<div class='sidebar-box'><h2>Campus Buddy</h2><p>Logged in as: Student</p></div>",
    unsafe_allow_html=True
)

st.session_state.page = st.sidebar.radio(
    "Navigation", ["Complaint", "Dashboard", "FAQs"], 
    index=["Complaint","Dashboard","FAQs"].index(st.session_state.page)
)

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.session_state.email = ""
    st.session_state.page = "Complaint"
    st.stop()  # Stop execution so the page reloads with login form

page = st.session_state.page

# COMPLAINT PAGE
if page == "Complaint":
    st.subheader("Submit a Complaint")
    st.markdown('<div class="complaint-card">', unsafe_allow_html=True)

    complaint_type = st.radio("Type", ["General", "Critical"], horizontal=True)
    selected_subcat = st.selectbox(
        "Category",
        list(general_categories.keys()) if complaint_type=="General" else list(critical_categories.keys())
    )
    st.caption(general_categories.get(selected_subcat,"") if complaint_type=="General" else critical_categories.get(selected_subcat,""))

    description = st.text_area("Describe your issue", height=120)
    anonymous = st.checkbox("Anonymous")
    file_path = None
    file = st.file_uploader("Attach file", type=["png","jpg","jpeg","pdf"])
    if file:
        os.makedirs("uploads", exist_ok=True)
        file_path = os.path.join("uploads", f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{file.name}")
        with open(file_path,"wb") as f: f.write(file.getbuffer())

    if st.button("Submit Complaint"):
        if description.strip()=="": st.warning("Enter a description")
        else:
            priority = "Urgent" if complaint_type=="Critical" else detect_priority(description)
            add_complaint(
                complaint_type, selected_subcat, selected_subcat,
                f"[{priority}] {description}", anonymous, file_path, st.session_state.email
            )
            st.success(f"Complaint submitted under {complaint_type} [{priority}]")
    st.markdown('</div>', unsafe_allow_html=True)

# DASHBOARD
elif page == "Dashboard":
    st.subheader("Dashboard - Complaints")
    complaints = get_all_complaints()
    if not complaints:
        st.info("No complaints yet.")
    else:
        for cid, ctype, category, subcategory, description, is_anonymous, file_path, email, status, assigned_to, created_at in complaints:
            # Only show complaints for this student
            if email != st.session_state.email and not is_anonymous: continue

            # Status colors: Pending → Red, In Progress → Yellow, Resolved → Green
            status_class = (
                "status-pending" if status=="Pending" else 
                "status-in-progress" if status=="In Progress" else 
                "status-resolved"
            )

            st.markdown(f'''
            <div class="complaint-card">
                <div class="status-bar {status_class}"></div>
                <b>{category} | {subcategory} — {status}</b><br>
                {description}
            </div>
            ''', unsafe_allow_html=True)

            if file_path: st.write(f"Attachment: {file_path}")

            # Only allow edit/withdraw for Pending complaints
            if status == "Pending":
                handle_edit_complaint(cid, description)
                handle_withdraw_complaint(cid)

# FAQ 
elif page == "FAQs":
    render_faqs(general_faqs, category_faqs)
