import json
import os

DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_expense():
    data = load_data()

    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    note = input("Enter note: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "note": note
    }

    data.append(expense)
    save_data(data)

    print("Expense added!")

def view_expenses():
    data = load_data()

    for e in data:
        print(e["date"], e["category"], e["amount"], e["note"])