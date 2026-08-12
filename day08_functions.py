# 'def' indicates a function. def function_name(parameters): -> def add(a, b)
def add(a, b):
    return a + b

summation = add(3,5)
print(summation)


def greet(name):
    return "Hello, " + name

print(greet("World"))

# If a func doesn' return anything, we do not use an return type as void
def log(message):
    print("LOG " + message)

result = log("Temp")
# Print statement will print None as log method doesn't return anything
print(result)

# Default arg function
# greeting attr is having a default value of Hello
def greet(name, greeting = "Hello"):
    return greeting +" "+ name

greeting = greet("World")
print(greeting)

#Overriding the default value
upgratedGreet = greet("World", "Hey")
print(upgratedGreet)

# Exponent is expressed as '**' similar to Math.pow in Java
def exp(base, exp = 2):
    return base ** exp

exponent = exp(2)
print(exponent)

exponent_one = exp(2,10)
print(exponent_one)

# Tuple unpacking. When function returns multiple values they are returned as tuples
def stats(nums):
    return min(nums), max(nums), sum(nums)

nums = [2,5,7,1,6]
low, high, total = stats(nums)
print(low, high, total)

# // - Floor division. % - Remainder
def division(a ,b):
    return a // b, a % b

q , r = division(23 ,7)
print(q, r)