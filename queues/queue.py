class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = -1
        self.size = 0
        self.rear = -1
        self.items = []

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, data):
        if self.size == self.capacity:
            print('no space!')
            return
        if self.size == 0:
            self.front += 1
        self.rear += 1
        self.items.append(data)
        self.size += 1
        print('%r has been enqueued'% data)

    def dqueue(self):
        if self.size == 0:
            print('empty queue!')
            return
        self.item = self.items[0]
        if self.size == 1:
            self.front -= 1
        self.items.pop(0)
        self.rear -= 1
        self.size -= 1
        return self.item

    def front(self):
        return self.items[0]
