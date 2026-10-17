class Expense:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"{self.description}: ${self.amount}"



class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add(self, expense):
        self.expenses.append(expense)

    def total(self):
        totalAmount = 0
        for expense in self.expenses:
            totalAmount += expense.amount
        return totalAmount

    def show_all(self):
        for exp in self.expenses:
            print(exp)
        print(f"Total: ${self.total()}")


tracker = ExpenseTracker()
tracker.add(Expense("Coffee", 5.0))
tracker.add(Expense("Lunch", 10.0))
tracker.show_all()