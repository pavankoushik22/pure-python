class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    # inserting at the starting of the linked list

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # inserting after a given node

    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print('given node should be in the linked list')
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # adding node at the end of the linked list

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_node(self, key):
        temp = self.head
        if self.head.data == key:
            self.head = temp.next
            temp = None
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def delete_at(self, position):
        if self.head is None:
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break
        if temp.next is None:
            return
        temp.next = temp.next.next

    def get_count(self):
        temp = self.head
        count = 0
        while (temp):
            count += 1
            temp = temp.next
        return count

    def get_rec_count(self, node):
        if not node:
            return 0
        else:
            return 1 + self.get_rec_count(node.next)

    def search(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    def search_recursive(self, node, data):
        if not node:
            return False
        if node.data == data:
            return True
        return self.search_recursive(node.next, data)

    def swap(self, x, y):
        if x == y:
            return False
        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next
        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next
        if prevX == None or prevY == None:
            return False
        prevX.next = currY
        prevY.next = currX
        temp2 = currX.next
        currX.next = currY.next
        currY.next = temp2

    def reverse(self):
        prev = None
        present = self.head
        future = self.head.next
        while future:
            present.next = prev
            prev = present
            present = future
            future = present.next
        self.head = present
        present.next = prev
        return True

    def detect_cycle(self):
        hare = self.head
        tortoise = self.head
        while hare:
            tortoise = tortoise.next
            temp = hare.next
            hare = temp.next
            if tortoise.data == hare.data:
                print('cycle found!')
                break
        return True


def sorted_merge(a, b):
    result = None
    if a == None:
        return b
    elif b == None:
        return a
    if a.data <= b.data:
        result = a
        result.next = sorted_merge(a.next, b)
    else:
        result = b
        result.next = sorted_merge(a, b.next)
    return result

def delete_alt(node):
    if node == None:
        return True
    rem = node.next
    if rem == None:
        return True
    node.next = rem.next
    print(node.data)
    del rem
    delete_alt(node.next)

def alt_split(node, a, b):
    temp = node
    while temp:
        a.append(temp.data)
        b.append(temp.next.data)
        if temp.next is None:
            break
        temp = temp.next.next
    return True

if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    four = Node(4)
    third.next = four
    llist2 = LinkedList()
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    llist2.head = five
    five.next = six
    six.next = seven

    llist.print_list()
    print('------------')
    aa = LinkedList()
    bb = LinkedList()
    alt_split(llist.head, aa, bb)
    aa.print_list()
    print('------------')
    bb.print_list()