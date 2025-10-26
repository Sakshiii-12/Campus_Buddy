# backend/auth.py
# Authentication module
ADMIN_EMAIL = "admin@college.edu"
ADMIN_PASSWORD = "Admin456"

STUDENT_EMAIL = "student@college.edu"
STUDENT_PASSWORD = "Student456"

# Functions to validate login credentials
def validate_student_login(email, password):
    return email == STUDENT_EMAIL and password == STUDENT_PASSWORD

def validate_admin_login(email, password):
    return email == ADMIN_EMAIL and password == ADMIN_PASSWORD
