import pandas as pd
import sqlite3

# Step 1: Load cleaned data
df = pd.read_csv("data/cleaned_electricity.csv")

# Step 2: Convert to list of dictionaries
bills = df.to_dict(orient="records")

# ---------------- FUNCTIONS ---------------- #

def show_all_bills():
    print("\n📋 All Electricity Bills:")
    for b in bills:
        print(f"Date: {b['date']}, Units: {b['electricity_kwh']}")

def modify_bill():
    date = input("\nEnter the date to modify (e.g., 2025-03-01): ")
    for b in bills:
        if b['date'] == date:
            print("Current data:", b)
            new_units = float(input("Enter new units consumed: "))
            b['electricity_kwh'] = new_units
            print("✅ Data updated successfully:", b)
            return
    print("❌ Date not found.")

def delete_bill():
    date = input("\nEnter the date to delete (e.g., 2025-03-01): ")
    for b in bills:
        if b['date'] == date:
            bills.remove(b)
            print("🗑️ Bill entry deleted successfully.")
            return
    print("❌ Date not found.")

def update_database_from_csv():
    """Reinsert all records from the CSV file into the database."""
    df = pd.read_csv("data/cleaned_electricity.csv")

    conn = sqlite3.connect("electricity.db")
    cursor = conn.cursor()

    # Clear the table before reinserting
    cursor.execute("DELETE FROM bills")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='bills'")

    # Insert all records again
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO bills (month, units, amount)
            VALUES (?, ?, ?)
        """, (row['date'], row['electricity_kwh'], row['electricity_kwh'] * 5))

    conn.commit()
    conn.close()
    print("✅ Database updated successfully!")

def save_changes():
    updated_df = pd.DataFrame(bills)
    updated_df.to_csv("data/cleaned_electricity.csv", index=False)
    update_database_from_csv()  # 🔥 keeps database in sync
    print("💾 Changes saved to cleaned_electricity.csv and database updated!")

# ---------------- MENU ---------------- #

while True:
    print("\n===== Electricity Bill Menu =====")
    print("1. Show all bills")
    print("2. Modify existing bill")
    print("3. Delete a bill")
    print("4. Save and exit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == '1':
        show_all_bills()
    elif choice == '2':
        modify_bill()
    elif choice == '3':
        delete_bill()
    elif choice == '4':
        save_changes()
        print("👋 Exiting menu...")
        break
    else:
        print("⚠️ Invalid choice. Please try again.")
