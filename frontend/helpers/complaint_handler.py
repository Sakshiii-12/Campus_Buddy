# frontend/helpers/complaint_handler.py
import streamlit as st
from backend.database import edit_complaint, delete_complaint

def handle_edit_complaint(cid, old_desc):
    # Show a form to edit a complaint. Updates DB on submission.
    
    key = f"edit_{cid}"
    with st.form(key):
        new_desc = st.text_area("Update your complaint", value=old_desc, key=key+"_ta")
        if st.form_submit_button("Save changes"):
            if new_desc.strip() == "":
                st.warning("Description cannot be empty.")
            else:
                edit_complaint(cid, new_desc)
                st.success("Complaint updated successfully.")
                st.experimental_rerun()

def handle_withdraw_complaint(cid):
    # Show a form to confirm withdrawal of a complaint.
    
    key = f"withdraw_{cid}"
    with st.form(key):
        if st.form_submit_button("Confirm Withdraw"):
            delete_complaint(cid)
            st.warning("Complaint withdrawn successfully.")
            st.experimental_rerun()
