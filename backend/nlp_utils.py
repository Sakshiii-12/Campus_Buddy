# backend/nlp_utils.py
def detect_priority(text):
    urgent_keywords = ["urgent", "immediately", "asap", "emergency", "help", "critical", "unsafe"]
    t = (text or "").lower()
    for kw in urgent_keywords:
        if kw in t:
            return "Urgent"
    return "Standard"
