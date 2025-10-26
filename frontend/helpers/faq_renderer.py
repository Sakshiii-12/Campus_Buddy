# frontend/helpers/faq_renderer.py
import streamlit as st

# FAQ Rendering
def render_faqs(general_faqs, category_faqs):
    st.subheader("General FAQs")
    for q, a in general_faqs:
        with st.expander(q):
            st.write(a)
    st.subheader("Category-Specific FAQs")
    for cat, faqs in category_faqs.items():
        with st.expander(cat):
            for faq in faqs:
                st.write(f"- {faq}")
