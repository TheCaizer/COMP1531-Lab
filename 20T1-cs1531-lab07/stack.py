class Stack:
    def __init__(self):
        self.dict = {}
        self.stck = 0

    def push(self, x):
        self.dict[self.stck] = x
        self.stck += 1

    def pop(self):
        res = self.dict[self.stck - 1]
        del self.dict[self.stck - 1]
        self.stck -= 1
        return res

def test_stack():
    stack = Stack()
    stack.push("Hello")
    stack.push("How are you?")
    stack.push("Goodbye")

    assert stack.pop() == "Goodbye"
    assert stack.pop() == "How are you?"
    assert stack.pop() == "Hello"