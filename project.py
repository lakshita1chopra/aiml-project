#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt

class Expense:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

class BudgetTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category].append(Expense(category, amount))
        else:
            self.expenses[category] = [Expense(category, amount)]

    def calculate_total_spending(self):
        total_spending = 0
        for expenses_list in self.expenses.values():
            total_spending += sum(expense.amount for expense in expenses_list)
        return total_spending

    def visualize_spending(self):
        categories = list(self.expenses.keys())
        amounts = [sum(expense.amount for expense in self.expenses[category]) for category in categories]

        plt.figure(figsize=(8, 6))
        plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title('Spending by Category')
        plt.show()


def main():
    budget_tracker = BudgetTracker()

    while True:
        print("\nBudget Tracker Menu:")
        print("1. Add Expense")
        print("2. View Total Spending")
        print("3. Visualize Spending")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            budget_tracker.add_expense(category, amount)
            print("Expense added successfully.")
        elif choice == '2':
            total_spending = budget_tracker.calculate_total_spending()
            print(f"Total Spending: ${total_spending:.2f}")
        elif choice == '3':
            budget_tracker.visualize_spending()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


# In[ ]:




