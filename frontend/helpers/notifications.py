# frontend/helpers/notifications.py
from backend.database import get_all_complaints

# Function to get user-specific notifications based on complaints
def get_user_notifications(user_email):
    notifications = []
    all_complaints = get_all_complaints()
    for cid, category, subcategory, description, is_anonymous, file_path, email, status, assigned_to, created_at in all_complaints:
        if not is_anonymous and user_email == email:
            notifications.append(f"Complaint [{category} | {subcategory}] is {status}")
        elif is_anonymous and user_email != "":
            notifications.append(f"Your anonymous complaint [{category} | {subcategory}] is {status}")
    notifications.reverse()
    return notifications