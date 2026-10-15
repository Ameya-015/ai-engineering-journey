class Note:
    def __init__(self, text):
        self.text = text
        self.length = len(text)

    def __str__(self):
        return f"Note[{self.length} chars]: {self.text}"

    def save(self, fileName):
        with open(fileName, "a") as a:
            a.write(str(self) + "\n")

n1 = Note("Buy Groceries")
n2 = Note("Call the bank")

n1.save("notes.txt")
n2.save("notes.txt")


def load_notes(filename):
    try:
        with open(filename, "r") as f:    
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("No notes found.")

load_notes("notes.txt")
load_notes("missing.txt")