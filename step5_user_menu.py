import pandas as pd
import sqlite3
from datetime import datetime

# --- Load data ---
df = pd.read_csv("data/cleaned_electricity.csv")
if "user_id" not in df.columns:
    df["user_id"] = 1
df["amount"] = df.get("amount", df["electricity_kwh"] * 5)
bills = df.to_dict("records")


def valid_date(d):
    try:
        datetime.strptime(d, "%Y-%m-%d")
        return True
    except:
        return False

# --- 1. View one user's data ---


def user_data():
    uid = int(input("Enter user ID: "))
    print(f"\n📋 Bills for User {uid}:")
    found = False
    for b in bills:
        if b["user_id"] == uid:
            print(
                f"Date: {b['date']} | Units: {b['electricity_kwh']} kWh | Amount: ₹{b['amount']:.2f}")
            found = True
    if not found:
        print("❌ No bills found for this user.")

# --- 2. Add new bill ---


def add_bill():
    uid = int(input("User ID: "))
    date = input("Date (YYYY-MM-DD): ")
    if not valid_date(date):
        return print("❌ Invalid date.")
    units = float(input("Units: "))
    bills.append({"user_id": uid, "date": date,
                  "electricity_kwh": units, "amount": units * 5})
    print("✅ Bill added!")

# --- 3. Show all bills ---


def show_bills():
    print("\n📋 All Electricity Bills:")
    for b in bills:
        print(
            f"User {b['user_id']} | {b['date']} | {b['electricity_kwh']} kWh | ₹{b['amount']:.2f}")

# --- 4. Delete a bill ---


def delete_bill():
    uid, date = int(input("User ID: ")), input("Date: ")
    for b in bills:
        if b["user_id"] == uid and b["date"] == date:
            bills.remove(b)
            return print("🗑️ Bill deleted!")
    print("❌ Bill not found!")

# --- 5. Save & Exit ---


def save_and_exit():
    pd.DataFrame(bills).to_csv("data/cleaned_electricity.csv", index=False)
    conn = sqlite3.connect("electricity.db")
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS bills")
    cur.execute(
        "CREATE TABLE bills(user_id INTEGER, month TEXT, units REAL, amount REAL)")
    cur.executemany("INSERT INTO bills VALUES(?,?,?,?)",
                    [(b["user_id"], b["date"], b["electricity_kwh"], b["amount"]) for b in bills])
    conn.commit()
    conn.close()
    print("💾 Saved successfully. Exiting...")


# --- Menu ---
while True:
    print("\n===== Electricity Bill Menu =====")
    print("1. User Data")
    print("2. Add New Bill")
    print("3. Show All Bills")
    print("4. Delete a Bill")
    print("5. Save and Exit")

    choice = input("\nEnter your choice (1–5): ")

    if choice == "1":
        user_data()
    elif choice == "2":
        add_bill()
    elif choice == "3":
        show_bills()
    elif choice == "4":
        delete_bill()
    elif choice == "5":
        save_and_exit()
        break
    else:
        print("⚠️ Invalid choice.")
