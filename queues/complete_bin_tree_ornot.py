from queues.queue import Queue
# for a binary tree ds
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_binary(root):
    flag = False
    if root is None:
        return False
    x = Queue(100)
    x.enqueue(root)
    while not x.is_empty():
        temp = x.dqueue()
        # if it is left node
        if temp.left:
            if flag:
                return False
            x.enqueue(temp.left)
        else:
            flag = True

        # if it is right node
        if temp.right:
            if flag:
                return False
            x.enqueue(temp.right)
        else:
            flag = True
    return True


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
if is_binary(root):
    print('yo yes boss!')
else:
    print('sry it is not')

