# Use case: If we want to transform the elements of a list and return those elements in a list we make use of comprehension
doubled = [] #empty list
for n in doubled:
    doubled.append(n * 2) #Appends is like arrayList.add()

# Alternative approach for above
updatedDoubled = [n * 2 for n in doubled] # Read it as 'n * 2 for each n in doubled'

nums = [10, 20, 30, 40]
result = [n * 10 for n in nums]
print(result)

# Similar to stream's .filter(), here we use trailing 'if'
nums = [1, 2, 3, 4, 5, 6, 7]
# general comprehension: [expression for var in source if condition]
# expression: Transformation, source: list/set, if - filtering condition
evens = [n for n in nums if n % 2 == 0]
print(evens)

# Combining filtering and transformation
nums = [1, 2, 3, 4, 5, 6, 7]
result = [n * n for n in nums if n % 2 == 0]
print(result)

