import pandas as pd
import sqlite3

# Step 1: Load the cleaned data
df = pd.read_csv("data/cleaned_electricity.csv")

# Step 2: Calculate bill amount (₹5 per unit)
df["amount"] = df["electricity_kwh"] * 5

# Step 3: Connect to the database
conn = sqlite3.connect("electricity.db")
cursor = conn.cursor()

# Step 4: Insert each row into the 'bills' table
cursor.execute("DELETE FROM bills")
cursor.execute("DELETE FROM sqlite_sequence WHERE name='bills'")
for index, row in df.iterrows():
    cursor.execute(
        "INSERT INTO bills (month, units, amount) VALUES (?, ?, ?)",
        (row["date"], row["electricity_kwh"], row["amount"])
    )
conn.commit()
conn.close()

print("✅ Bills calculated and stored in the database!")
