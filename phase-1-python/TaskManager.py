class Task:
    def __init__(self, title, done = False):
        self.title = title
        self.done = done

    def __str__(self):
        if self.done != True:
            return f"[ ] {self.title}"
        else:
            return f"[x] {self.title}"

# t1 = Task("Buy Milk")
# t2 = Task("Buy chocolate")

# print(t1)
# print(t2)


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add(self, title):
        self.tasks.append(Task(title, False))

    def complete(self, index):
        try:
            self.tasks[index].done = True
        except IndexError:
            print("No task at that number")

    def list_tasks(self):
        for idx, task in enumerate(self.tasks):
            idx += 1
            print(f"{idx}. {task}")

    def pending_count(self):
        count = 0
        for task in self.tasks:
            if not task.done:
                count += 1
        return count

    def save(self, filename):
        with open(filename, "w") as f:
            for task in self.tasks:
                index = 0
                if(task.done == True):
                    index = 1

                f.write(f"{index}|{task.title}\n")

    def load(self, filename):
        try:
            with open(filename) as f:
                for line in f:
                    text = line.strip().split("|")
                    if(int(text[0]) == 1):
                        t = Task(text[1])
                        t.done = True
                        self.tasks.append(t)
                    else:
                        t = Task(text[1])
                        self.tasks.append(t)
                return self.tasks
        except FileNotFoundError:
            self.tasks = []


t = TaskManager()
t.load("testingList.txt")
t.list_tasks()
# t.add("Buy milk")
# print(t.pending_count())
# t.complete(0)
# print(t.pending_count())
# t.list_tasks()

# t.save("tasksList.txt")
# t1 = TaskManager()
# t1.load("tasksList.txt")
# print(t.list_tasks())

# CLI Interactive loop
if __name__ == "__main__":
    tm = TaskManager()
    tm.load("testingList.txt")

    while True:
        choice = input("Command (add/list/done/quit): ")
        if choice == "add":
            title = input("Enter the task title: ")
            tm.add(title)
        elif choice == "list":
            tm.list_tasks()
        elif choice == "done":
            try:
                number = int(input("Enter a number: "))
                tm.complete(number - 1)
            except ValueError:
                print("Enter a valid number")
        elif choice == "quit":
            tm.save("testingList.txt")
            break
        else:
            print("Unkown command.")
    

