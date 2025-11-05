import pandas as pd
import sqlite3

# Load the cleaned data
df = pd.read_csv("data/cleaned_electricity.csv")
if "user_id" not in df.columns:
    df["user_id"] = 1
df["amount"] = df["electricity_kwh"] * 5

# Connect to database
conn = sqlite3.connect("electricity.db")
cur = conn.cursor()

# ---- Drop old table and recreate clean table ----
cur.execute("DROP TABLE IF EXISTS bills")
cur.execute("""
CREATE TABLE bills(
 user_id INTEGER,
 month TEXT,
 units REAL,
 amount REAL
)
""")

# ---- Insert data ----
for _, r in df.iterrows():
    cur.execute("INSERT INTO bills(user_id, month, units, amount) VALUES (?, ?, ?, ?)",
                (r["user_id"], r["date"], r["electricity_kwh"], r["amount"]))

conn.commit()
conn.close()
print("✅ Bills stored successfully (no 'id' column)!")
