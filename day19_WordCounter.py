class WordCounter:
    def __init__(self):
        self.counts = {}

    def add_word(self, word):
        self.counts[word] = self.counts.get(word, 0) + 1

    def add_sentence(self, sentance):
        wordsList = sentance.split()
        for word in wordsList:
            self.add_word(word)

    def report(self):
        for word, count in self.counts.items():
            print(f"{word}: {count}")


counter = WordCounter()
counter.add_sentence("the cat sat on the mat")
counter.add_sentence("the dog sat")
counter.report()

def load_and_count(filename):
    new_counter = WordCounter()
    try:
        with open(filename, "r") as f:
            for line in f:
                new_counter.add_sentence(line.strip())
        return new_counter
    except FileNotFoundError:
        print("File not Found")
        return None

c = load_and_count("sample.txt")
if c:
    c.report()

load_and_count("nope.txt")