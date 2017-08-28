from stacks.stack import Stack
#using strategy of making enqueue costly

class q:
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.size = 0
        # from stk1 pop will be done
        self.stk1 = Stack()
        # stk2 is used to shift data while enq
        self.stk2 = Stack()

    def enq(self, data):
        if self.size == 0:
            self.front += 1
            self.rear += 1
            self.size += 1
            self.stk1.push(data)
        else:
            self.rear += 1
            self.size += 1
            while not self.stk1.is_empty():
                self.stk2.push(self.stk1.peek())
                self.stk1.pop()
            self.stk1.push(data)
            while not self.stk2.is_empty():
                self.stk1.push(self.stk2.peek())
                self.stk2.pop()

    def dq(self):
        if self.size == 1:
            self.front -= 1
            self.rear -= 1
            self.size -= 1
            self.temp = self.stk1.peek()
            self.stk1.pop()
            return self.temp
        elif self.size == 0:
            print('queue is empty!')
            return 0
        else:
            self.temp = self.stk1.peek()
            self.stk1.pop()
            return self.temp

if __name__ == "__main__":
    x = q()
    x.enq(1)
    x.enq(2)
    print(x.dq())
