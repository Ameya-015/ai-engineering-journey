
def safeDivide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return (f"Cannot divide by 0")


print(safeDivide(10,2))
print(safeDivide(10,0))
print(safeDivide(9,3))