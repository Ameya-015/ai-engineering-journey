# self is Java's 'this'. It is ALWAYS the first parameter of every method.
# __init__ : This is the constructor

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")

d = Dog("Golden Retreiver")
d.bark()


class Counter:
    def __init__(self, count):
        self.count = count

    def increment(self):
        self.count = self.count + 2

    def decrement(self):
        self.count = self.count - 1

    def show(self):
        print(f"Count is: {self.count}")

c = Counter(5)
c.increment()
c.decrement()
c.show()

############################################################################################

# Exercise
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def show(self):
        print(f"Balance: {self.balance}")

b = BankAccount(100)
b.deposit(50)
b.withdraw(30)
b.show()
