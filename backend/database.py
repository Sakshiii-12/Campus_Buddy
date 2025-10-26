# backend/database.py
import sqlite3
from datetime import datetime

DB_PATH = "complaints.db"

# INIT DB
def init_db():
    
    # Initialize database and create complaints table if not exists.
    # Ensures all required columns are present.
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # Create table with all columns
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
def add_complaint(ctype, category, subcategory, description, is_anonymous, file_path, email):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute(
        '''INSERT INTO complaints 
           (type, category, subcategory, description, is_anonymous, file_path, email, status, created_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
        (ctype, category, subcategory, description, int(is_anonymous), file_path, email, "Pending", created_at)
    )
    conn.commit()
    conn.close()

# GET ALL COMPLAINTS
def get_all_complaints():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM complaints ORDER BY created_at DESC")
    rows = c.fetchall()
    conn.close()
    return rows

# UPDATE STATUS
def update_complaint_status(cid, status):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE complaints SET status=? WHERE id=?", (status, cid))
    conn.commit()
    conn.close()

# ASSIGN COMPLAINT
def assign_complaint(cid, staff):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE complaints SET assigned_to=? WHERE id=?", (staff, cid))
    conn.commit()
    conn.close()

# EDIT COMPLAINT 
def edit_complaint(cid, new_desc):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE complaints SET description=? WHERE id=?", (new_desc, cid))
    conn.commit()
    conn.close()

# DELETE COMPLAINT
def delete_complaint(cid):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM complaints WHERE id=?", (cid,))
    conn.commit()
    conn.close()