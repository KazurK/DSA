class node:
    def __init__(self, value):
        self.value = value
        self.next = None

class stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        newNode = node(value)
        if self.head:
            newNode.next = self.head
        self.head = newNode
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        poppedNode = self.head
        self.head = self.head.next
        self.size -= 1
        return poppedNode.value

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.value

    def isEmpty(self):
        return self.size == 0

    def stackSize(self):
        return self.size

myStack = stack()
myStack.push("A")
myStack.push('B')
myStack.push('C')

print("Pop: ", myStack.pop())
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.stackSize())
