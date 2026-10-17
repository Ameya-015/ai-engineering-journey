def clean_and_split(raw):
    rawList = raw.split(",")
    cleanedList = [line.strip().lower() for line in rawList]
    return cleanedList

print(clean_and_split("  Apple , BANANA ,  Cherry  "))