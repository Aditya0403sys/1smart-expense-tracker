from expense_manager import load_data
import matplotlib.pyplot as plt

def total_spending():
    data = load_data()

    total = sum(e["amount"] for e in data)

    print("Total spending:", total)

def category_analysis():

    data = load_data()

    categories = {}

    for e in data:
        cat = e["category"]
        categories[cat] = categories.get(cat, 0) + e["amount"]

    for c,a in categories.items():
        print(c, a)

    return categories

def show_graph():

    data = category_analysis()

    names = list(data.keys())
    values = list(data.values())

    plt.bar(names, values)

    plt.title("Expense Analysis")

    plt.xlabel("Category")
    plt.ylabel("Amount")

    plt.show()