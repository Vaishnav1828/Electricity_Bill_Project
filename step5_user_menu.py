import pandas as pd
import sqlite3
from datetime import datetime

# Step 1: Load data
df = pd.read_csv("data/cleaned_electricity.csv")
bills = df.to_dict(orient="records")

# Function to check if date is valid (YYYY-MM-DD)


def valid_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except:
        return False

# Add new bill


def add_bill():
    date = input("Enter date (YYYY-MM-DD): ")
    if not valid_date(date):
        print("❌ Invalid date! Example: 2025-03-01")
        return

    # Check if date already exists
    for b in bills:
        if b['date'] == date:
            print("⚠️ Bill already exists for this date!")
            return

    try:
        units = float(input("Enter units consumed: "))
    except:
        print("❌ Please enter a valid number!")
        return

    bills.append({"date": date, "electricity_kwh": units})
    print("✅ Bill added successfully!")

# Show all bills


def show_bills():
    print("\n📋 All Electricity Bills:")
    for b in bills:
        print(f"Date: {b['date']} | Units: {b['electricity_kwh']} kWh")

# Modify bill


def modify_bill():
    date = input("Enter date to modify (YYYY-MM-DD): ")
    if not valid_date(date):
        print("❌ Invalid date!")
        return

    for b in bills:
        if b['date'] == date:
            print(f"Current units: {b['electricity_kwh']}")
            try:
                new_units = float(input("Enter new units: "))
            except:
                print("❌ Invalid number!")
                return
            b['electricity_kwh'] = new_units
            print("✅ Bill updated successfully!")
            return
    print("❌ Bill not found!")

# Delete bill


def delete_bill():
    date = input("Enter date to delete (YYYY-MM-DD): ")
    if not valid_date(date):
        print("❌ Invalid date!")
        return

    for b in bills:
        if b['date'] == date:
            bills.remove(b)
            print("🗑️ Bill deleted successfully!")
            return
    print("❌ Bill not found!")

# Save all changes to CSV + Database


def save_and_exit():
    pd.DataFrame(bills).to_csv("data/cleaned_electricity.csv", index=False)

    conn = sqlite3.connect("electricity.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM bills")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='bills'")

    for b in bills:
        cursor.execute(
            "INSERT INTO bills (month, units, amount) VALUES (?, ?, ?)",
            (b['date'], b['electricity_kwh'], b['electricity_kwh'] * 5)
        )

    conn.commit()
    conn.close()
    print("💾 Changes saved successfully! Exiting...")


# ===== MENU =====
while True:
    print("\n===== Electricity Bill Menu =====")
    print("1. Add new bill")
    print("2. Show all bills")
    print("3. Modify existing bill")
    print("4. Delete a bill")
    print("5. Save and exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == '1':
        add_bill()
    elif choice == '2':
        show_bills()
    elif choice == '3':
        modify_bill()
    elif choice == '4':
        delete_bill()
    elif choice == '5':
        save_and_exit()
        break
    else:
        print("⚠️ Invalid choice. Please try again.")
print("asgdsahdbckjsdbkjsdjbcnew2")
