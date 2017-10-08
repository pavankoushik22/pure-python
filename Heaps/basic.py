from heapq import heappush, heappop, heapify


class Minheap:
    def __init__(self):
        self.heap = []

    def parent(self,  i):
        return (i -1)//2

    def insertKey(self, value):
        heappush(self.heap, value)

    def decreaseKey(self, i, new_value):
        self.heap[i] = new_value
        while i !=0 and self.heap[self.parent(i)] > self.heap[i] :
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
        # use heapify (builtin) function instead of this looping

    def extractMin(self):
        return heappop(self.heap)

    def deleteKey(self, i):
        self.decreaseKey(i, float("-inf"))
        self.extractMin()

    def getMin(self):
        return self.heap[0]



