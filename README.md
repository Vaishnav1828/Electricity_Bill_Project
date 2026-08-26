# ⚡ Electricity Bill Project

This is a simple Python project to manage electricity bills using **lists**, **dictionaries**, and **CSV files** (without SQL database).  
It helps calculate, modify, and delete monthly electricity consumption data easily.

## 📋 Features
- Load and clean electricity data  
- View all bills  
- Modify existing bill records  
- Delete unwanted bill entries  
- Save updated data back to CSV  

## 🛠️ Technologies Used
- Python  
- Pandas (for CSV handling)  

## 📁 File Overview
| File Name | Description |
|------------|-------------|
| `step1_load_data.py` | Loads and cleans electricity data |
| `step2_create_db.py` | Creates database (optional version) |
| `step3_calculate_bills.py` | Calculates bill amount from electricity units |
| `step4_view_bills.py` | Displays stored bill data |
| `step5_user_menu.py` | Provides a user menu for modify/delete operations |
| `data/cleaned_electricity.csv` | Cleaned electricity dataset |

## 🧠 How to Run
1. Open your terminal in VS Code.  
2. Navigate to your project folder:  
   ```bash
   cd D:\Electricity_Bill_Project
   ```
3. Run the main menu program:
   ```bash
   python step5_user_menu.py
   ```

> **Note:** Update the project path above if you cloned the repository to a different folder.
