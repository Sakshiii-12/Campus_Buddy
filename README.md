# Campus Buddy: AI-Powered Complaint Management System

**Campus Buddy** is an intelligent, web-based complaint and feedback management system built for colleges and universities. It integrates **AI (Gemini API)** and **NLP-powered automation** to make grievance handling faster, smarter, and more transparent for both students and administrators.



## Overview

Students often face slow complaint resolutions or lack updates, while administrators struggle to organize and prioritize issues efficiently.
**Campus Buddy** bridges this gap with a single, intelligent platform that provides:

* AI-assisted categorization and sentiment analysis
* Smart dashboards for actionable insights
* An integrated chatbot (rule-based + Gemini AI hybrid)
* Efficient admin workflows with filters, assignment, and real-time status updates



## Key Features

### Student Portal

* Register **General** or **Critical** complaints with optional file attachments
* Submit complaints **anonymously** for open communication
* NLP-based **auto-priority detection** (*Urgent / Standard*)
* View complaint history and assigned departments
* Track complaint status in real time (*Pending → In Progress → Resolved*)
* Built-in **Gemini + Rule-Based Chatbot** for FAQs and quick help
* Clean, responsive UI with color-coded status cards



### Admin Portal

* Secure **Admin Login** for complaint management

* **Filter and Assign Panel**

  * Filter complaints by *Category*, *Status*, or *Date Range*
  * Assign issues to departments or staff members
  * Instant feedback on successful assignment

* **Smart NLP Insights**

  * **Sentiment Analysis** — Understand complaint tone (*Positive / Neutral / Negative*)
  * **Keyword Extraction** — Identify common themes and concerns
  * **Auto Category Suggestion** — Predicts the most relevant complaint category

* **Visual Dashboards**

  * Complaint distribution by *status* and *category*
  * Sentiment-based bar charts for quick analysis

* Export complaints as **CSV files** for reporting and records



## Chatbot (Rule-Based + Gemini Hybrid)

Campus Buddy features a **dual-mode chatbot system** that combines rule-based FAQs with AI intelligence for open-ended questions.
Each chatbot reply clearly mentions its source:
**(Campus Buddy — Instant Answer)** or **(Campus Buddy — Smart Assistant)**

| Mode                            | Description                                               | Example Response                                                                       |
| ------------------------------- | --------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **Rule-Based (Instant Answer)** | Fast, fuzzy-matched responses for predefined FAQs.        | “You can collect a new ID card from the Admin Office, Block A.”                        |
| **Gemini Smart Assistant**      | Uses Google’s Gemini API for contextual, natural answers. | “Try scheduling short study sessions and taking regular breaks to manage exam stress.” |



## How It Works

Campus Buddy combines traditional complaint management with intelligent automation, following a simple yet powerful flow:

1. **Students Submit Complaints**

   * Through a structured form that accepts text, attachments, and anonymous submissions.
   * The system analyzes the text using NLP to detect urgency and sentiment.

2. **NLP Engine Processes Data**

   * Keywords and tone are extracted from complaint text.
   * The system auto-suggests categories like *Infrastructure*, *Hostel*, or *Faculty*.

3. **Admin Dashboard Visualization**

   * Complaints appear in real time, sorted by priority or sentiment.
   * Admins can update status, assign tasks, and filter records using the built-in dashboard.

4. **Chatbot Assistance**

   * Students can interact with Campus Buddy’s chatbot for quick FAQs or detailed AI-generated help.
   * The chatbot switches automatically between rule-based and Gemini AI responses.

5. **Continuous Feedback Loop**

   * As complaints are resolved, data contributes to trend analysis and institutional insights for improvement.



## NLP-Powered Intelligence

Campus Buddy integrates advanced NLP (Natural Language Processing) to make complaint handling context-aware and efficient.

| Feature                      | Description                                                             |
| ---------------------------- | ----------------------------------------------------------------------- |
| **Priority Detection**       | Detects urgency using keywords like *urgent*, *unsafe*, or *emergency*. |
| **Sentiment Analysis**       | Evaluates tone — *Positive, Neutral,* or *Negative*.                    |
| **Keyword Extraction**       | Identifies key nouns and terms for quicker categorization.              |
| **Auto Category Suggestion** | Predicts the most suitable complaint category from the text.            |



## Project Structure

```
CampusBuddy/
│
├── backend/
│   ├── auth.py             # Authentication for students and admins
│   ├── chatbot.py          # Gemini + rule-based chatbot integration
│   ├── config.py           # Category and subcategory mappings
│   ├── database.py         # SQLite database and CRUD operations
│   └── nlp_utils.py        # Sentiment, keyword, and priority detection
│
├── frontend/
│   ├── app.py              # Student portal (complaint form + chatbot)
│   ├── admin_app.py        # Admin portal with filters and analytics
│   └── helpers/
│       ├── charts.py       # Complaint visualization components
│       └── styles.py       # Custom CSS and UI styling
│
├── uploads/                # Uploaded attachments
├── complaints.db           # SQLite database file
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```



## Installation Guide

### 1. Clone the Repository

```bash
git clone <repository-url>
cd CampusBuddy
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Applications

```bash
# Student Portal
streamlit run frontend/app.py

# Admin Portal
streamlit run frontend/admin_app.py
```



## Login Credentials (Demo)

| Role        | Email                 | Password     |
| ----------- | --------------------- | ------------ |
| **Student** | `student@college.edu` | `Student456` |
| **Admin**   | `admin@college.edu`   | `Admin456`   |



## Tech Stack

| Layer             | Technologies                |
| ----------------- | --------------------------- |
| **Frontend**      | Streamlit, Plotly, HTML/CSS |
| **Backend**       | Python, SQLite              |
| **NLP and AI**      | TextBlob, NLTK, Gemini API  |
| **Visualization** | Plotly             |
| **Data Export**   | CSV                         |
