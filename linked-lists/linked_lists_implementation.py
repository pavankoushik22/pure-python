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
