import sqlite3
import pandas as pd

conn = sqlite3.connect("electricity.db")
df = pd.read_sql_query("SELECT * FROM bills", conn)
conn.close()

print("📋 All Electricity Bills:")
print(df if not df.empty else "No data found! Run Step 3 first.")
