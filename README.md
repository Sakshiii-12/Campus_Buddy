# Campus Buddy - Complaint Management System

**Campus Buddy** is a comprehensive web-based platform designed to streamline complaint management and feedback collection in college environments. The system ensures that student grievances, infrastructure issues, and administrative concerns are submitted, tracked, and resolved efficiently. By providing both student-facing and admin-facing interfaces, Campus Buddy improves transparency, accountability, and communication within the campus community.



## Overview

Students often face challenges in reporting complaints such as delayed responses, miscommunication, or lack of clarity on whom to contact. Similarly, college administrators need an organized way to manage, assign, and resolve complaints while maintaining data for reporting and analysis.

**Campus Buddy** addresses these challenges by offering:

* **Structured Complaint Submission**: Categorized as General or Critical, allowing students to specify the type and nature of their grievance.
* **Anonymous Submissions**: Students can submit complaints without revealing their identity, encouraging honest reporting.
* **Priority Detection**: Critical complaints are highlighted automatically, and text-based priority detection ensures urgent matters are attended promptly.
* **Admin Tools**: Administrators can view all complaints, update statuses, assign responsibilities, filter by category or date, and export data for reporting.
* **Analytics and Insights**: Visual charts showing complaints by status and category provide actionable insights for campus management.
* **FAQs and Help**: Both general and category-specific FAQs guide students on complaint submission and resolution processes.



## Key Features

**Student Portal**

* Submit complaints with detailed descriptions and file attachments (images, PDFs).
* Choose between General or Critical complaint types.
* Submit anonymously if desired.
* Edit or withdraw complaints that are still pending.
* Dashboard displaying status of all submitted complaints.
* Access FAQs for guidance on common issues.

**Admin Portal**

* Secure login for administrators.
* View all complaints with complete details.
* Update complaint statuses: Pending, In Progress, Resolved.
* Assign complaints to staff or departments.
* Filter complaints by category, status, and date.
* Export complaint data to CSV files.
* Analytics with charts for complaints by status and category.

**Backend Utilities**

* SQLite database for persistent storage of complaints and metadata.
* NLP-based priority detection for urgent complaints.
* Functions to add, edit, delete, and assign complaints programmatically.



## Project Structure

```
CampusBuddy/
│
├── backend/                       # Core backend functionality
│   ├── auth.py                    # Handles authentication for students and admins
│   ├── config.py                  # Complaint categories and FAQs
│   ├── database.py                # Database operations (add, edit, delete complaints)
│   └── nlp_utils.py               # Detect priority of complaints
│
├── frontend/                      # Frontend applications
│   ├── app.py                     # Student portal
│   ├── admin_app.py               # Admin portal
│   └── helpers/                   # Helper modules
│       ├── charts.py              # Visualizations using Plotly
│       ├── complaint_handler.py   # Edit and withdraw complaints
│       ├── faq_renderer.py        # Display FAQs
│       ├── navbar.py              # Navigation bar
│       ├── notifications.py       # User-specific notifications
│       └── styles.py              # CSS styling for UI
│
├── uploads/                        # Uploaded files for complaints
├── complaints.db                   # SQLite database (auto-created)
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```



## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd CampusBuddy
```

2. Create a Python virtual environment and activate it:

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. Run the Streamlit applications:

```bash
# Student portal
streamlit run frontend/app.py

# Admin portal
streamlit run frontend/admin_app.py
```



## Login credentials:

1. Student Portal
  * Email: `student@college.edu`
  * Password: `Student456`

2. Admin Portal
  * Email: `admin@college.edu`
  * Password: `Admin456`


## Screenshot of main pages

1. Admin main page
<img width="1898" height="780" alt="Image" src="https://github.com/user-attachments/assets/aca26755-d136-4871-b05c-858eaebd2477" />

2. Student main page
<img width="1901" height="782" alt="Image" src="https://github.com/user-attachments/assets/1a68fb31-2113-48f8-8781-69bc5454697d" />



## Technology Stack

* Python 3.11+
* Streamlit for web interfaces
* SQLite for database management
* Pandas for data manipulation
* Plotly for interactive charts



## Future Enhancements

* Role-based user registration and authentication.
* Automated email notifications for students and staff.
* AI-powered complaint categorization for faster processing.
* Advanced dashboards with trend analysis.
* Mobile-responsive design for better accessibility.
