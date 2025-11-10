# backend/chatbot.py
import difflib
import google.generativeai as genai

# Configure Gemini API directly (replace with your actual API key)
genai.configure(api_key="YOUR_GEMINI_API_KEY")

# Category-specific FAQs
category_faqs = {
    "Academics and Faculty": [
        ("Where can I find my timetable?", "You can check your timetable on the student portal."),
        ("Who do I contact for grading errors?", "Please reach out to your course coordinator or faculty member."),
        ("Can I request lecture recordings?", "That depends on the course policy and faculty permission.")
    ],
    "Administration and Services": [
        ("Where to get new ID cards?", "You can collect a new ID card from the Admin Office, Block A."),
        ("Fee payment deadlines?", "Please refer to the official college portal for fee deadlines."),
        ("Lost ID card?", "Visit the admin desk and submit a replacement request.")
    ],
    "Infrastructure and Facilities": [
        ("Who fixes AC/light issues?", "Facilities management handles such issues. You can report it through Campus Buddy."),
        ("How to report broken benches?", "Please file a complaint under 'Infrastructure and Facilities' in Campus Buddy.")
    ],
    "Hostel and Transportation": [
        ("Van schedule?", "You can check the van schedule at the transport office notice board."),
        ("Hostel maintenance issues?", "Contact the hostel supervisor or submit a maintenance complaint.")
    ],
    "Connectivity and Hygiene": [
        ("Wi-Fi issues?", "Reach out to the IT helpdesk for Wi-Fi-related concerns."),
        ("Cleanliness complaints?", "You can report cleanliness issues through Campus Buddy.")
    ],
    "Sports and Activities": [
        ("Joining clubs?", "Get in touch with the student council for club registrations."),
        ("Equipment issues?", "Visit the sports office to report any damaged or missing equipment.")
    ],
    "Library": [
        ("Book not available?", "You can request the book from the librarian."),
        ("Room booking?", "Contact the library helpdesk for room reservations."),
        ("Library card lost?", "Apply for a replacement card at the admin block.")
    ]
}

# General FAQs
general_faqs = [
    ("How long will it take to resolve my complaint?", "Most complaints are resolved within 3–5 working days."),
    ("Can I submit anonymously?", "Yes, you can. Your name will not appear in your complaint history."),
    ("Can I edit my complaint?", "No, editing is not supported yet. This feature will be available soon."),
    ("What happens after submission?", "Your complaint is forwarded to the relevant department for review."),
    ("What types of issues can I report?", "You can report academic, infrastructure, faculty, hostel, or transport issues."),
    ("Can I attach multiple files?", "Currently, you can attach only one image or document per complaint."),
    ("How do I track my complaint status?", "You can check your complaint status under the 'My Complaints' section."),
    ("Can I change my registered email?", "Please contact the administration office to update your registered email.")
]


# RULE-BASED CHATBOT
def get_rule_based_response(user_input: str) -> str | None:
    # Try to answer from rule-based FAQs.
    msg = (user_input or "").strip().lower()

    # Greetings
    if any(greet in msg for greet in ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]):
        return "Hello! I’m Campus Buddy. How can I help you today?"

    # Flatten FAQs
    all_questions = [q for cat in category_faqs.values() for q, _ in cat] + [q for q, _ in general_faqs]
    all_answers = [a for cat in category_faqs.values() for _, a in cat] + [a for _, a in general_faqs]

    # Fuzzy match (find closest question)
    match = difflib.get_close_matches(msg, all_questions, n=1, cutoff=0.6)
    if match:
        idx = all_questions.index(match[0])
        return all_answers[idx]

    return None


# GEMINI FALLBACK
def get_gemini_response(prompt: str) -> str:
    # Fallback to Gemini API if no rule-based match.
    try:
        # Corrected model name for the current API
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(
            f"You are Campus Buddy, a formal and concise virtual assistant for a college. "
            f"Respond politely and professionally to the following student question:\n\n{prompt}"
        )

        if hasattr(response, "text") and response.text:
            return response.text.strip()
        else:
            return "I'm sorry, I couldn’t process that right now."
    except Exception as e:
        return f"Sorry, I couldn’t connect to the Gemini API. ({e})"

# MAIN FUNCTION
def get_chatbot_response(user_input: str):
    # Returns both chatbot text and response source type.
    # 1. Try rule-based first
    rule_response = get_rule_based_response(user_input)
    if rule_response:
        return rule_response, "rule"

    # 2. If no match, use Gemini
    gemini_response = get_gemini_response(user_input)
    if gemini_response:
        return gemini_response, "gemini"

    # Fallback (shouldn’t happen)
    return "I'm not sure how to answer that right now.", "unknown"
