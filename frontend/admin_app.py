# frontend/admin_app.py
# Campus Buddy Admin Portal

import streamlit as st
import pandas as pd
import sys, os, time
from datetime import datetime, date  # for date filtering

# Fix Python path so backend imports work
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Imports
from backend.database import get_all_complaints, update_complaint_status, assign_complaint, init_db
from backend.auth import validate_admin_login
from backend.nlp_utils import get_sentiment_label, extract_keywords, suggest_category
from backend.config import general_categories, critical_categories
from frontend.helpers.charts import show_status_pie_chart, show_category_pie_chart
from frontend.helpers.styles import load_custom_css, render_navbar

# PAGE CONFIG AND STYLE
st.set_page_config(page_title="Campus Buddy Admin", layout="wide", page_icon="🛠️")
load_custom_css()
init_db()

# LOGIN CHECK
if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

# ADMIN LOGIN PAGE
if not st.session_state.admin_logged_in:
    render_navbar("Welcome to Campus Buddy")
    st.title("Admin Login")
    with st.form("admin_login"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.form_submit_button("Login"):
            if validate_admin_login(email, password):
                st.session_state.admin_logged_in = True
                st.rerun()
            else:
                st.error("Invalid credentials.")
    st.stop()

# SIDEBAR NAVIGATION
st.sidebar.title("Admin Panel")
page = st.sidebar.radio("Navigate", ["Dashboard", "All Complaints", "Filters - Assign", "Export"])
if st.sidebar.button("Logout"):
    st.session_state.admin_logged_in = False
    st.rerun()

# LOAD DATA
rows = get_all_complaints()
df = pd.DataFrame(rows, columns=[
    "id", "type", "category", "subcategory", "description", "is_anonymous",
    "file_path", "email", "status", "assigned_to", "created_at"
])

# DASHBOARD
if page == "Dashboard":
    render_navbar("Dashboard — Complaint Summary")

    if df.empty:
        st.info("No complaints yet.")
    else:
        total = len(df)
        pending = len(df[df['status'] == 'Pending'])
        in_progress = len(df[df['status'] == 'In Progress'])
        resolved = len(df[df['status'] == 'Resolved'])

        st.markdown("### Overview")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total", total)
        c2.metric("Pending", pending)
        c3.metric("In Progress", in_progress)
        c4.metric("Resolved", resolved)

        st.divider()

        # Charts Section 
        st.markdown("### Complaints Breakdown")
        show_status_pie_chart(rows)
        show_category_pie_chart(rows)

        # Sentiment Analysis Chart
        st.markdown("### Complaint Sentiment")
        df["Sentiment"] = df["description"].apply(get_sentiment_label)
        sentiment_counts = df["Sentiment"].value_counts().reset_index()
        sentiment_counts.columns = ["Sentiment", "Count"]
        st.bar_chart(sentiment_counts.set_index("Sentiment"))

# ALL COMPLAINTS
elif page == "All Complaints":
    render_navbar("All Complaints")

    if df.empty:
        st.info("No complaints available.")
    else:
        for _, r in df.iterrows():
            # Subtle color indicator based on status
            if r.status == "Resolved":
                border_color = "#28a745"  # green
            elif r.status == "In Progress":
                border_color = "#ffc107"  # yellow
            else:
                border_color = "#dc3545"  # red

            # Assigned text safely handled
            assigned_display = r.assigned_to if r.assigned_to else "Not yet assigned"

            html_content = f"""
                <div style="
                    border-left: 8px solid {border_color};
                    padding: 10px 15px;
                    margin-bottom: 12px;
                    border-radius: 6px;
                    background-color: #ffffff;
                    box-shadow: 0 1px 3px rgba(0,0,0,0.08);
                ">
                    <strong>ID {r.id} — {r.type}</strong><br>
                    <strong>Category:</strong> {r.category}<br>
                    <strong>Status:</strong> 
                        <span style='color:{border_color}; font-weight:600;'>{r.status}</span><br>
                    <strong>Description:</strong> {r.description}<br>
            """

            if r.file_path:
                html_content += f"<strong>Attachment:</strong> {r.file_path}<br>"
            html_content += f"<strong>Assigned to:</strong> {assigned_display}</div>"

            st.markdown(html_content, unsafe_allow_html=True)

            # Show extracted keywords and suggested category
            keywords = extract_keywords(r.description)
            st.caption(f"**Keywords:** {', '.join(keywords) if keywords else 'N/A'}")
            suggested_cat = suggest_category(r.description, {**general_categories, **critical_categories})
            st.caption(f"**Suggested Category:** {suggested_cat}")

            # Update status
            new_status = st.selectbox(
                f"Update status for ID {r.id}",
                ["Pending", "In Progress", "Resolved"],
                index=["Pending", "In Progress", "Resolved"].index(r.status),
                key=f"status_{r.id}",
            )
            if st.button(f"Set status {r.id} ➜ {new_status}", key=f"update_{r.id}"):
                update_complaint_status(r.id, new_status)
                st.success(f"Updated status to {new_status}")
                time.sleep(1)
                st.rerun()

# FILTERS - ASSIGN
elif page == "Filters - Assign":
    render_navbar("Filter - Assign")

    if df.empty:
        st.info("No complaints available.")
    else:
        cats = ["All"] + sorted(df['category'].unique().tolist())
        statuses = ["All"] + sorted(df['status'].unique().tolist())

        c1, c2, c3, c4 = st.columns(4)
        with c1:
            selected_cat = st.selectbox("Filter by category", cats)
        with c2:
            selected_status = st.selectbox("Filter by status", statuses)
        with c3:
            date_from = st.date_input("From")
        with c4:
            date_to = st.date_input("To")

        # Convert created_at to Python datetime safely
        filtered = df.copy()
        filtered["created_at_dt"] = filtered["created_at"].apply(
            lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S") if isinstance(x, str) else x
        )

        # Apply filters
        if selected_cat != "All":
            filtered = filtered[filtered["category"] == selected_cat]
        if selected_status != "All":
            filtered = filtered[filtered["status"] == selected_status]
        if date_from:
            filtered = filtered[filtered["created_at_dt"].dt.date >= date_from]
        if date_to:
            filtered = filtered[filtered["created_at_dt"].dt.date <= date_to]

        if not filtered.empty:
            summary = filtered["status"].value_counts().to_dict()
            st.caption(
                f"Summary — Pending: {summary.get('Pending', 0)} | "
                f"In Progress: {summary.get('In Progress', 0)} | "
                f"Resolved: {summary.get('Resolved', 0)}"
            )

        st.divider()

        for _, r in filtered.iterrows():
            with st.expander(f"{r.id} — {r.type} / {r.category} — {r.status}"):

                st.markdown(f"<strong>Description:</strong> {r.description}", unsafe_allow_html=True)

                if r.file_path:
                    st.markdown(f"<strong>Attachment:</strong> {r.file_path}", unsafe_allow_html=True)

                assigned_display = r.assigned_to if r.assigned_to else "Not yet assigned"
                st.markdown(f"<strong>Assigned to:</strong> {assigned_display}", unsafe_allow_html=True)

                staff = st.text_input(
                    f"Assign to (staff/department) for complaint {r.id}",
                    value=r.assigned_to or "",
                    key=f"assign_{r.id}"
                )

                if st.button(f"Assign Complaint #{r.id}", key=f"assign_btn_{r.id}"):
                    if staff.strip() == "":
                        st.warning("Please enter a staff or department name before assigning.")
                    else:
                        assign_complaint(r.id, staff)
                        st.success(f"Complaint {r.id} successfully assigned to {staff}.")
                        time.sleep(1.5)
                        st.rerun()

# EXPORT DATA
elif page == "Export":
    render_navbar("Export Complaints")

    if df.empty:
        st.info("No complaints to export.")
    else:
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "Download All Complaints",
            data=csv,
            file_name="campus_buddy_complaints.csv",
            mime="text/csv",
        )
        st.markdown("### Data Preview")
        st.dataframe(df.head(50))
