# Dictionary comprehension
nums = [1, 2, 3, 4]
result = {n: n * n for n in nums}
print(result)

# Set comprehension
nums = [1, 2, 2, 3, 3, 4]
uniqueSquares = {n * n for n in nums}
print(uniqueSquares)

words = ["hi", "hello", "hey"]
words_dict = {w : len(w) for w in words}
print(words_dict)

# f-strings: Formatted string: We use for concatenation with non-string variables
day = 10
name = "Demo"
xp = 100
msg = f"Day {day}: {name} earned {xp} XP"
print(msg)

# Format how values appears inside braces with a :(colon)
price = 3.14159
print(f"{price:.2f}") # 3.14 - Decimal digits formatted upto 2 places

pct = 0.847
print(f"{pct:.1%}") # 84.7 - Multiplies by 100 and addes %