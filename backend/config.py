# backend/config.py
# Categories
general_categories = {
    "Academics and Faculty": "Timetable, grading, faculty unavailability",
    "Administration and Services": "Fee payment, ID cards, library services",
    "Infrastructure and Facilities": "AC, lights, classrooms, labs, benches, water",
    "Hostel and Transportation": "Mess, room maintenance, vans, parking",
    "Connectivity and Hygiene": "Wi-Fi, internet, cleanliness, sanitation",
    "Sports and Activities": "Gym, sports equipment, clubs",
    "Library": "Books, study rooms, access issues"
}

critical_categories = {
    "Bullying and Harassment": "Verbal/physical bullying, harassment",
    "Mental Health": "Stress, anxiety, counseling",
    "Discrimination": "Bias based on gender, caste, religion, ethnicity",
    "Safety": "Unsafe environment, stalking, threats"
}

# Category-specific FAQs
category_faqs = {
    "Academics and Faculty": [
        "Where can I find my timetable? Check the online portal.",
        "Who do I contact for grading errors? Course coordinator.",
        "Can I request lecture recordings? Depends on course policy."
    ],
    "Administration and Services": [
        "Where to get new ID cards? Admin office, Block A.",
        "Fee payment deadlines? Check portal notifications.",
        "Lost ID card? File an application at admin desk."
    ],
    "Infrastructure and Facilities": [
        "Who fixes AC/light issues? Facilities management.",
        "How to report broken benches? File a complaint in Campus Buddy."
    ],
    "Hostel and Transportation": [
        "Van schedule? Transport office.",
        "Hostel maintenance issues? Hostel supervisor."
    ],
    "Connectivity and Hygiene": [
        "Wi-Fi issues? Contact IT helpdesk.",
        "Cleanliness complaints? Campus facilities."
    ],
    "Sports and Activities": [
        "Joining clubs? Student council.",
        "Equipment issues? Sports office."
    ],
    "Library": [
        "Book not available? Request with librarian.",
        "Room booking? Library helpdesk.",
        "Library card lost? Admin block."
    ]
}

# General FAQs
general_faqs = [
    ("How long will it take to resolve my complaint?", "Most complaints are addressed within 3–5 working days."),
    ("Can I submit anonymously?", "Yes. Your name will not appear in history if you choose to stay anonymous."),
    ("Can I edit my complaint?", "You can edit or delete it as long as it’s still pending."),
    ("What happens after submission?", "Your complaint goes to the relevant department for review and resolution."),
    ("What types of issues can I report?", "Academics, infrastructure, faculty, hostel, mess, transport, and more."),
    ("Can I attach multiple files?", "Yes, you can attach images or documents to support your complaint."),
    ("How do I track my complaint status?", "You can view the status (Pending/In Progress/Resolved) under History."),
    ("Can I change my registered email?", "Yes, you can update it in your profile settings."),
    ("Forgot password? How do I reset?", "Use the 'Forgot Password' option on the login page.")
]
