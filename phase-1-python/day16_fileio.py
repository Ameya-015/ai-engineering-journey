with open("fruits.txt", "w") as f:
    f.write("mango\n")
    f.write("apple\n")
    f.write("grape\n")

with open("fruits.txt", "r") as r:
    for line in r:
        print(line.strip())
