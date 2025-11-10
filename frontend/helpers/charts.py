# frontend/helpers/charts.py
# Chart utilities for CampusBuddy Admin Dashboard

import pandas as pd
import streamlit as st
import plotly.express as px
from backend.nlp_utils import get_sentiment_label  # updated NLP

COMPLAINT_COLUMNS = [
    "id", "type", "category", "subcategory", "description", "is_anonymous",
    "file_path", "email", "status", "assigned_to", "created_at"
]

def complaints_df_from_rows(rows):
    # Convert raw DB rows to DataFrame using shared schema
    return pd.DataFrame(rows, columns=COMPLAINT_COLUMNS)

def show_status_pie_chart(rows):
    # Display a pie chart of complaints by status
    df = complaints_df_from_rows(rows)
    if df.empty:
        return st.info("No complaints to display.")
    counts = df["status"].value_counts()
    fig = px.pie(
        names=counts.index,
        values=counts.values,
        color=counts.index,
        color_discrete_map={"Pending":"#FFB703","In Progress":"#219EBC","Resolved":"#8AC926"},
        title="Complaints by Status"
    )
    fig.update_traces(textposition="inside", textinfo="percent+label")
    fig.update_layout(showlegend=True, template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)

def show_category_pie_chart(rows):
    # Display a pie chart of complaints by category
    df = complaints_df_from_rows(rows)
    if df.empty:
        return st.info("No complaints to display.")
    counts = df["category"].value_counts()
    fig = px.pie(names=counts.index, values=counts.values, title="Complaints by Category")
    fig.update_traces(textposition="inside", textinfo="percent+label")
    fig.update_layout(showlegend=True, template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)

def show_sentiment_bar_chart(rows):
    # Display a bar chart of complaints by sentiment (Positive/Neutral/Negative)
    df = complaints_df_from_rows(rows)
    if df.empty:
        return st.info("No complaints to display.")
    
    # Apply sentiment detection to all descriptions
    df["Sentiment"] = df["description"].apply(get_sentiment_label)
    sentiment_counts = df["Sentiment"].value_counts().reset_index()
    sentiment_counts.columns = ["Sentiment", "Count"]
    fig = px.bar(
        sentiment_counts,
        x="Sentiment",
        y="Count",
        color="Sentiment",
        color_discrete_map={"Positive":"#4CAF50","Neutral":"#FFC107","Negative":"#F44336"},
        title="Complaint Sentiment"
    )
    st.plotly_chart(fig, use_container_width=True)
