# backend/nlp_utils.py
# NLP utilities for Campus Buddy — sentiment, priority, keyword extraction, auto-category suggestion

import re

# Try importing TextBlob for sentiment analysis
try:
    from textblob import TextBlob
    _HAS_TEXTBLOB = True
except Exception:
    _HAS_TEXTBLOB = False

# Try importing spaCy for keyword extraction
try:
    import spacy
    nlp = spacy.load("en_core_web_sm")
    _HAS_SPACY = True
except Exception:
    _HAS_SPACY = False

# Priority Detection
def detect_priority(text: str) -> str:
    # Detect if a complaint is urgent based on keywords.
    # Returns 'Urgent' or 'Standard'.
    urgent_words = [
        "urgent", "immediately", "asap", "emergency",
        "help", "critical", "unsafe", "danger", "important", "right away"
    ]
    t = (text or "").lower()
    return "Urgent" if any(kw in t for kw in urgent_words) else "Standard"

# Sentiment Analysis
def get_sentiment_label(text: str) -> str:
    # Returns sentiment label: 'Positive', 'Neutral', 'Negative'.
    # Uses TextBlob if available, else a fallback heuristic.
    t = (text or "").strip()
    if t == "":
        return "Neutral"

    if _HAS_TEXTBLOB:
        try:
            polarity = TextBlob(t).sentiment.polarity
            if polarity > 0.1:
                return "Positive"
            if polarity < -0.1:
                return "Negative"
            return "Neutral"
        except Exception:
            pass

    # Fallback simple keyword heuristic
    pos = ["good", "great", "satisfied", "happy", "excellent", "resolved"]
    neg = ["bad", "poor", "angry", "upset", "problem", "not", "never", "complaint", "frustrat", "issue", "hate"]
    score = 0
    tl = t.lower()
    for w in pos: 
        if w in tl: score += 1
    for w in neg: 
        if w in tl: score -= 1
    if score > 0: return "Positive"
    if score < 0: return "Negative"
    return "Neutral"

# Keyword / Tag Extraction
def extract_keywords(text: str, top_n: int = 5) -> list:
    # Extract top N keywords or noun phrases from complaint text.
    
    if not text:
        return []
    if _HAS_SPACY:
        doc = nlp(text)
        keywords = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]
        chunks = [chunk.text for chunk in doc.noun_chunks]
        all_keywords = list(set(keywords + chunks))
    else:
        words = re.findall(r'\b\w{4,}\b', text.lower())
        all_keywords = list(set(words))
    return all_keywords[:top_n]

# Auto-Category Suggestion
def suggest_category(description: str, categories_dict: dict) -> str:
    # Suggest the most relevant category based on description keywords.
    # Returns best match or 'Other'.
    description = (description or "").lower()
    max_score = 0
    suggested = None
    for cat, keywords in categories_dict.items():
        score = sum(description.count(word.strip().lower()) for word in keywords.split(","))
        if score > max_score:
            max_score = score
            suggested = cat
    return suggested or "Other"
