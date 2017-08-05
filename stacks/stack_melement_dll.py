class StackNode:
    def __init__(self, data, prev, next):
        self.data =data
        self.prev = None
        self.next = None


class Stack:
    count = 0
    root = None
    mid = None

    def __init__(self):
        self.root = None

    def isEmpty(self):
        return True if self.root is None else False

    def push(self, data):
        new_node = StackNode(data, None, None)
        if self.root is None:
            self.root = new_node
        else:
            new_node.next = self.root
        self.count += 1
        self.root.prev = new_node
        if self.count == 1:
            self.mid = new_node
        else:
            self.root.prev = new_node
            if self.count % 2 != 0:
                self.mid = self.mid.prev
        self.root = new_node

    def pop(self):
        if self.isEmpty():
            return float('-inf')
        temp = self.root
        self.root = self.root.next
        self.root.prev = None
        self.count = self.count - 1
        if self.count % 2 == 0:
            self.mid = self.mid.next

        return temp.data

    def findMiddle(self):
        if self.count == 0:
            print('stack is empty: ')
            return -1
        return self.mid.data

stk = Stack()
stk.push(2)
stk.push(3)
stk.push(4)
print(stk.findMiddle())


