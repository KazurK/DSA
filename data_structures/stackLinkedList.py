class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        newNode = Node(value)
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


