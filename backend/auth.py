# backend/auth.py
# Admin credentials
ADMIN_EMAIL = "admin@college.edu"
ADMIN_PASSWORD = "Admin456"

# Student credentials
STUDENT_EMAIL = "student@college.edu"
STUDENT_PASSWORD = "Student456"

def validate_student_login(email, password):
    # Check student login credentials.
    return email == STUDENT_EMAIL and password == STUDENT_PASSWORD

def validate_admin_login(email, password):
    # Check admin login credentials.
    return email == ADMIN_EMAIL and password == ADMIN_PASSWORD
