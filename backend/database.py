# backend/database.py
import sqlite3
from datetime import datetime

DB_PATH = "complaints.db"

# DATABASE INITIALIZATION
def init_db():
    # Create complaints table if it does not exist.
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS complaints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT,
            category TEXT,
            subcategory TEXT,
            description TEXT,
            is_anonymous INTEGER,
            file_path TEXT,
            email TEXT,
            status TEXT DEFAULT 'Pending',
            assigned_to TEXT,
            created_at TEXT
        )
    ''')
    conn.commit()
    conn.close()

# ADD COMPLAINT
def add_complaint(ctype, category, subcategory, description, anon, file_path, email):
    # Insert a new complaint into the database.
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        INSERT INTO complaints 
        (type, category, subcategory, description, is_anonymous, file_path, email, status, assigned_to, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, 'Pending', NULL, ?)
    ''', (ctype, category, subcategory, description, int(anon), file_path, email, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

# FETCH COMPLAINTS
def get_all_complaints():
    # Fetch all complaints from the database
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM complaints ORDER BY created_at DESC")
    rows = c.fetchall()
    conn.close()
    return rows

def get_complaints_by_email(email):
    # Fetch all complaints submitted by a specific student.
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM complaints WHERE email=? ORDER BY created_at DESC", (email,))
    rows = c.fetchall()
    conn.close()
    return rows

# UPDATE COMPLAINT
def update_complaint_status(cid, new_status):
    # Update status of a complaint by ID.
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE complaints SET status=? WHERE id=?", (new_status, cid))
    conn.commit()
    conn.close()

def assign_complaint(cid, staff_name):
    # Assign complaint to staff/department.
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE complaints SET assigned_to=? WHERE id=?", (staff_name, cid))
    conn.commit()
    conn.close()

def delete_complaint(cid):
    # Delete complaint by ID.
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM complaints WHERE id=?", (cid,))
    conn.commit()
    conn.close()
