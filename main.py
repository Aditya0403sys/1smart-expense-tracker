from expense_manager import add_expense, view_expenses
from analytics import total_spending, category_analysis, show_graph
while True:

    print("\nSMART EXPENSE TRACKER")

    print("1 Add Expense")
    print("2 View Expenses")
    print("3 Total Spending")
    print("4 Category Analysis")
    print("5 Graph")
    print("6 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_spending()

    elif choice == "4":
        category_analysis()

    elif choice == "5":
        show_graph()

    elif choice == "6":
        break

    else:
        print("Invalid choice")