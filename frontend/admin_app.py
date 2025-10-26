# frontend/admin_app.py
import sys, os
sys.path.insert(0, os.path.abspath("."))

import streamlit as st
import pandas as pd
from datetime import datetime

from backend.database import init_db, get_all_complaints, update_complaint_status, assign_complaint
from backend.auth import validate_admin_login
from frontend.helpers.styles import global_styles
from frontend.helpers.navbar import render_navbar
from frontend.helpers.charts import complaints_df_from_rows, show_status_pie_chart, show_category_pie_chart

init_db()
st.set_page_config(page_title="Campus Buddy Admin", layout="centered", page_icon="🎓")
st.markdown(global_styles, unsafe_allow_html=True)

# SESSION
if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

# LOGIN
if not st.session_state.admin_logged_in:
    render_navbar("Campus Buddy Admin")
    st.subheader("Admin Login")
    with st.form("admin_login"):
        email = st.text_input("Admin Email")
        password = st.text_input("Password", type="password")
        if st.form_submit_button("Login"):
            if validate_admin_login(email, password):
                st.session_state.admin_logged_in = True
                st.success("Admin login successful.")
                st.stop()  # Stop execution here, page will reload automatically
            else:
                st.error("Invalid admin credentials.")
    st.stop()  # Ensure nothing else renders before login

# MAIN ADMIN PAGE
st.sidebar.markdown(
    f"<div class='sidebar-box'><h2>Campus Buddy Admin</h2><p>Logged in as: Admin</p></div>",
    unsafe_allow_html=True
)

page = st.sidebar.radio("Navigation", ["Dashboard","All Complaints","Filters - Assign","Analytics","Export"])

if st.sidebar.button("Logout"):
    st.session_state.admin_logged_in = False
    st.stop()  # Stop execution so login page shows immediately

# Fetch complaints once
rows = get_all_complaints()
df = complaints_df_from_rows(rows)

# DASHBOARD
if page=="Dashboard":
    render_navbar("Campus Buddy Admin")
    st.subheader("Dashboard - Notifications")
    st.info(f"Total complaints: {len(df)}")
    pending = len(df[df['status']=='Pending'])
    in_progress = len(df[df['status']=='In Progress'])
    resolved = len(df[df['status']=='Resolved'])
    st.markdown(f"- Pending: {pending}\n- In Progress: {in_progress}\n- Resolved: {resolved}")

# ALL COMPLAINTS 
elif page=="All Complaints":
    render_navbar("All Complaints")
    if df.empty:
        st.info("No complaints available.")
    else:
        for _, r in df.iterrows():
            with st.expander(f"ID {r.id} — {r.type} / {r.category} — {r.status}"):
                st.write(r.description)
                if r.file_path: st.write(f"Attachment: {r.file_path}")
                new_status = st.selectbox(
                    f"Update status for ID {r.id}", 
                    ["Pending","In Progress","Resolved"], 
                    index=["Pending","In Progress","Resolved"].index(r.status),
                    key=f"status_{r.id}"
                )
                if st.button(f"Set status {r.id} ➜ {new_status}", key=f"update_{r.id}"):
                    update_complaint_status(r.id, new_status)
                    st.success(f"Updated status to {new_status}")
                    st.stop()  # Stop execution to reload page

# FILTERS - ASSIGN 
elif page=="Filters - Assign":
    render_navbar("Filter - Assign")
    if df.empty:
        st.info("No complaints available.")
    else:
        cats = ["All"] + sorted(df['category'].unique().tolist())
        statuses = ["All"] + sorted(df['status'].unique().tolist())
        selected_cat = st.selectbox("Filter by category", cats)
        selected_status = st.selectbox("Filter by status", statuses)
        date_from = st.date_input("From", value=None)
        date_to = st.date_input("To", value=None)

        filtered = df.copy()
        if selected_cat != "All": filtered = filtered[filtered['category']==selected_cat]
        if selected_status != "All": filtered = filtered[filtered['status']==selected_status]
        if date_from: filtered = filtered[filtered['created_at'].astype('datetime64') >= pd.to_datetime(date_from)]
        if date_to: filtered = filtered[filtered['created_at'].astype('datetime64') <= pd.to_datetime(date_to)]

        st.markdown(f"Showing {len(filtered)} complaints after filters")
        for _, r in filtered.iterrows():
            with st.expander(f"ID {r.id} — {r.type} / {r.category} — {r.status}"):
                st.write(r.description)
                if r.file_path: st.write(f"Attachment: {r.file_path}")
                staff = st.text_input(f"Assign to (staff/department) for {r.id}", value=r.assigned_to or "", key=f"assign_{r.id}")
                if st.button(f"Assign {r.id}", key=f"assign_btn_{r.id}"):
                    assign_complaint(r.id, staff)
                    st.success(f"Assigned complaint {r.id} to {staff}")
                    st.stop()  # Stop execution to reload page

# ANALYTICS 
elif page=="Analytics":
    render_navbar("Analytics")
    if df.empty: st.info("No complaints to analyze.")
    else:
        st.markdown("Complaints by Status")
        show_status_pie_chart(rows)
        st.markdown("Complaints by Category")
        show_category_pie_chart(rows)

# EXPORT
elif page=="Export":
    render_navbar("Export Complaints")
    if df.empty: st.info("No complaints to export.")
    else:
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download CSV", data=csv, file_name="campus_buddy_complaints.csv", mime="text/csv")
        st.markdown("Data preview:")
        st.dataframe(df.head(100))
