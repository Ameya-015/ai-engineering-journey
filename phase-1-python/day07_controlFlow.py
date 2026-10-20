# if elif else block
x = 14
if x > 10:
    print("Big")
elif x > 6 and x <= 9: #In python we use direct literals for && and || -> and, or
    print("Medium")
else:
    print("Small")


# for loop -> For each is the default for loop in Python
langs = ["Java", "Python", "Ruby"]
for lang in langs: # read it as -> for each variable in source -> for each lang in langs
    print(lang) #prints the obj on a new line

# index based iteration in for loop. 
# Enurmerate wraps the source and provides index and the value each time
for i, lang in enumerate(langs):
    print(i, lang)

# Ranged for loop in python -> range(5) = for(int i = 0; i < 5; i++)
for i in range(5):
    print(i)

for i in range(1,5):
    print(i)