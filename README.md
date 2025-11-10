# Campus Buddy: AI-Powered Complaint Management System

**Campus Buddy** is a smart web-based platform that helps colleges and universities manage student complaints efficiently. It uses **AI (Gemini API)** and **Natural Language Processing (NLP)** to make grievance handling faster, more transparent, and data-driven for both students and administrators.


## Overview

Students often face delays and poor communication when submitting complaints.
Administrators, on the other hand, struggle to categorize, prioritize, and respond to issues efficiently.

**Campus Buddy** bridges this gap by offering:

* AI-assisted categorization and sentiment analysis
* Smart dashboards for quick insights
* An integrated hybrid chatbot for instant help
* Easy-to-use admin tools for filtering, assigning, and updating complaints


## Key Features

### Student Portal

* Submit **General** or **Critical** complaints with or without attachments
* Choose to file complaints **anonymously**
* Automatic **priority detection** based on urgency
* Track complaint progress (*Pending → In Progress → Resolved*)
* View assigned department or staff for your complaint
* Built-in **Gemini + Rule-Based Chatbot** for FAQs and academic support
* Clean, responsive design with color-coded complaint cards


### Admin Portal

* Secure login for admins
* **Filter and Assign Panel** to sort complaints by category, status, or date
* Assign complaints to relevant staff or departments
* Real-time success confirmation when a complaint is assigned
* **NLP Insights** to detect sentiment, extract keywords, and suggest categories
* Interactive charts showing complaint distribution and sentiment trends
* Export complaint data as CSV for audits and reporting


## Chatbot

Campus Buddy includes a smart chatbot that works in two ways:
Each message clearly states its source: **(Campus Buddy - Instant Answer)** or **(Campus Buddy - Smart Assistant)**.

1. **Rule-Based Mode** — Instantly answers predefined FAQs such as library hours, ID card replacement, or academic contacts.
2. **Gemini AI Mode** — Handles open-ended, conversational queries using Google’s Gemini API, providing personalized, context-aware guidance.


## How It Works

1. **Students Submit Complaints** through a simple online form.
2. **NLP Analysis** identifies keywords, sentiment, and urgency.
3. **Admins Review and Assign** complaints through a filtered dashboard.
4. **Chatbot Assists** students with instant help or AI-powered advice.
5. **Insights Emerge** — The system identifies recurring issues for better decision-making.


## NLP-Powered Intelligence

Campus Buddy’s NLP engine automatically detects urgency, mood, and themes within student complaints.
It performs:

* **Priority Detection** – Flags critical complaints instantly.
* **Sentiment Analysis** – Measures tone (positive, neutral, or negative).
* **Keyword Extraction** – Pulls important terms for context.
* **Category Suggestion** – Suggests the best-fit complaint category.

This allows admins to act faster and understand campus-wide issues at a glance.


## Project Structure

```
CampusBuddy/
│
├── backend/
│   ├── auth.py          # Authentication
│   ├── chatbot.py       # Gemini + rule-based chatbot
│   ├── config.py        # Complaint categories
│   ├── database.py      # SQLite operations
│   └── nlp_utils.py     # NLP functions (sentiment, keywords)
│
├── frontend/
│   ├── app.py           # Student portal
│   ├── admin_app.py     # Admin dashboard
│   └── helpers/
│       ├── charts.py    # Visualization logic
│       └── styles.py    # Custom styling
│
├── uploads/             # File uploads
├── complaints.db        # SQLite database
└── README.md            # Documentation
```


## Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd CampusBuddy
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the applications**

   ```bash
   # Student Portal
   streamlit run frontend/app.py

   # Admin Portal
   streamlit run frontend/admin_app.py
   ```


## Demo Login

* **Student** — `student@college.edu` / `Student456`
* **Admin** — `admin@college.edu` / `Admin456`


## Tech Stack

* **Frontend:** Streamlit, Plotly, HTML/CSS
* **Backend:** Python, SQLite
* **NLP and AI:** TextBlob, NLTK, Gemini API
* **Visualization:** Plotly
* **Data Export:** CSV


## Future Enhancements

* Email and notification alerts for new complaints
* Multi-language chatbot support
* Admin report exports (PDF format)
* AI-driven clustering to detect issue patterns
* Sentiment tracking over time
