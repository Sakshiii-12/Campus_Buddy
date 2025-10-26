# frontend/helpers/charts.py
import pandas as pd
import streamlit as st
import plotly.express as px
from backend.database import get_all_complaints

# Data Preparation
def complaints_df_from_rows(rows):
    df = pd.DataFrame(rows, columns=[
        "id", "type", "category", "subcategory", "description", "is_anonymous",
        "file_path", "email", "status", "assigned_to", "created_at"
    ])
    return df

# Visualizations
def show_status_pie_chart(rows):
    df = complaints_df_from_rows(rows)
    if df.empty: return st.info("No complaints to display.")
    counts = df['status'].value_counts()
    fig = px.pie(names=counts.index, values=counts.values, color=counts.index,
                 color_discrete_map={"Pending":"#FFB703","In Progress":"#219EBC","Resolved":"#8AC926"},
                 title="Complaints by Status")
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig, use_container_width=True)

def show_category_pie_chart(rows):
    df = complaints_df_from_rows(rows)
    if df.empty: return st.info("No complaints to display.")
    counts = df['category'].value_counts()
    fig = px.pie(names=counts.index, values=counts.values, title="Complaints by Category")
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig, use_container_width=True)