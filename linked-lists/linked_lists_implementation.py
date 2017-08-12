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
        for i in range(position-1):
            temp = temp.next
            if temp is None:
                break
        if temp.next is None:
            return
        temp.next = temp.next.next

    def get_count(self):
        temp = self.head
        count = 0
        while(temp):
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




if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    llist.append(4)
    llist.push(5)
    llist.insert_after(second, 7)
    llist.print_list()
    llist.delete_node(4)
    print('------------')
    llist.print_list()
    llist.delete_at(1)
    print('------------')
    llist.print_list()