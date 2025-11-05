import pandas as pd
import sqlite3
from datetime import datetime

# Load CSV
df = pd.read_csv("data/cleaned_electricity.csv")
if "user_id" not in df.columns:
    df["user_id"] = 1
bills = df.to_dict(orient="records")


def valid_date(d):
    try:
        datetime.strptime(d, "%Y-%m-%d")
        return True
    except:
        return False

# ---- 1. View a user's data ----


def user_data():
    uid = int(input("Enter user ID to view: "))
    print(f"\n📋 Bills for User {uid}:")
    found = False
    for b in bills:
        if b["user_id"] == uid:
            print(f"Date: {b['date']} | Units: {b['electricity_kwh']} kWh")
            found = True
    if not found:
        print("❌ No bills found for this user.")

# ---- 2. Add new bill ----


def add_bill():
    uid = int(input("Enter user ID: "))
    date = input("Enter date (YYYY-MM-DD): ")
    if not valid_date(date):
        print("❌ Invalid date!")
        return
    units = float(input("Enter units: "))
    bills.append({"user_id": uid, "date": date, "electricity_kwh": units})
    print("✅ Bill added!")

# ---- 3. Show all bills ----


def show_bills():
    for b in bills:
        print(
            f"User {b['user_id']} | {b['date']} | {b['electricity_kwh']} kWh")

# ---- 4. Modify existing bill ----


def modify_bill():
    uid = int(input("User ID: "))
    date = input("Date: ")
    for b in bills:
        if b["user_id"] == uid and b["date"] == date:
            b["electricity_kwh"] = float(input("New units: "))
            print("✅ Bill updated!")
            return
    print("❌ Bill not found!")

# ---- 5. Delete a bill ----


def delete_bill():
    uid = int(input("User ID: "))
    date = input("Date: ")
    for b in bills:
        if b["user_id"] == uid and b["date"] == date:
            bills.remove(b)
            print("🗑️ Bill deleted!")
            return
    print("❌ Bill not found!")

# ---- 6. Save and Exit ----


def save_and_exit():
    # save to CSV
    pd.DataFrame(bills).to_csv("data/cleaned_electricity.csv", index=False)

    # rebuild DB table cleanly (no 'id' column)
    conn = sqlite3.connect("electricity.db")
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS bills")
    cur.execute("""
        CREATE TABLE bills(
          user_id INTEGER,
          month TEXT,
          units REAL,
          amount REAL
        )
    """)
    for b in bills:
        cur.execute("INSERT INTO bills(user_id,month,units,amount) VALUES(?,?,?,?)",
                    (b["user_id"], b["date"],
                     b["electricity_kwh"],
                     b["electricity_kwh"] * 5))
    conn.commit()
    conn.close()
    print("💾 Saved. Bye!")


# ===== MENU =====
while True:
    print("\n===== Electricity Bill Menu =====")
    print("1. User Data")
    print("2. Add New Bill")
    print("3. Show All Bills")
    print("4. Modify Existing Bill")
    print("5. Delete a Bill")
    print("6. Save and Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        user_data()
    elif choice == "2":
        add_bill()
    elif choice == "3":
        show_bills()
    elif choice == "4":
        modify_bill()
    elif choice == "5":
        delete_bill()
    elif choice == "6":
        save_and_exit()
        break
    else:
        print("⚠️ Invalid choice!")
