class queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

testQueue = queue()
testQueue.enqueue("A")
testQueue.enqueue("B")
testQueue.enqueue("C")
testQueue.enqueue("D")

print("Queue", testQueue.queue) #Expected: A, B, C, D
print("Dequeue", testQueue.dequeue()) #Expected: A
print("Peek", testQueue.peek()) #Expected: B
print("isEmpty: ", testQueue.isEmpty())
print("Size: ", testQueue.size())

