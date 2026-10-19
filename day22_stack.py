class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, item):
        self.stack_list.append(item)

    def pop(self):
        item = self.stack_list.pop()
        return item

    def size(self):
        return len(self.stack_list)



stack = Stack()
stack.push("Tea")
stack.push("Sugar")
stack.push("Salt")

stack.pop()
print(stack.size())