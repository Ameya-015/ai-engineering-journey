#Dunder methods - __init__ , __eq__ and __str__

# Dunder methods wire the objects directly into Python's operator or build-in functions

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

a = Money(100, "USD")
b = Money(100, "USD")
c = Money(100, "EUR")

print(a)
print(a == b)
print(a == c)
