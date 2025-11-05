# step2_create_db.py
import sqlite3

# Connect to a database file (it will be created automatically)
conn = sqlite3.connect("electricity.db")
cursor = conn.cursor()

# Create a table to store bills
cursor.execute("""
CREATE TABLE IF NOT EXISTS bills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    month TEXT,
    units REAL,
    amount REAL
)
""")

conn.commit()
conn.close()

print("✅ Database and table created successfully!")
