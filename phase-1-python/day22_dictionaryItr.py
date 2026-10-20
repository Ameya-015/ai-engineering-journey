def count_words(text):
    words = text.split()
    dict = {}

    for elm in words:
        dict[elm] = dict.get(elm, 0) + 1

    return dict

print(count_words("the cat the dog"))


def safe_load(filename):
    list = []
    try:
        with open(filename) as f:
            for line in f:
                list.append(line.strip())
        return list
    except FileNotFoundError:
        return list

print(safe_load("None.txt"))