import sqlite3
import pandas as pd

# Step 1: Connect to the database
conn = sqlite3.connect("electricity.db")

# Step 2: Read all data from the 'bills' table
df = pd.read_sql_query("SELECT * FROM bills", conn)

conn.close()

# Step 3: Display the data
print("📊 Electricity Bills Data:")
print(df)
