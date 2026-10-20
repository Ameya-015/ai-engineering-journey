# Tuples: Behaves like list but it is immutable. Similar to List.of() which returns an immutable list 
# list - [], set - ()

tuples = (1,2,3,4,5,6);
print(tuples[1])
print(tuples[0:4])


# When a function returns more than one value Python uses a tuple to achieve this.

def min_max(tuples):
    return min(tuples), max(tuples)

low, high = min_max(tuples)

print(low)
print(high)

# Dict keys should be immutable. A list can't be a key in dict but a tuple can.
# {(0, 0) : origin} is valid as the key is a tuple. But, {[0,0] : origin} is invalid as key is a list


def divide(a, b):
    return a // b, a % b

# '//' indicates a int division value. It will return the floor value of the expression
# '/' in Python will always return a float value of the division.