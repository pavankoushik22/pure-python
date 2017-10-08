def utility(node, data):
    if node is None:
        return 0
    if node.data == data:
        if node.left:
            temp = node.left
            while temp.right:
                temp = temp.right
            utility.pre = temp.data
        if node.right:
            temp2 = node.right
            while temp2.left:
                temp2 = temp2.left
            utility.succ = temp2.data
        return 0

    if node.data > data:
        utility.succ = node.data
        utility(node.left, data)
    else:
        utility.pre = node.data
        utility(node.right, data)



class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


def insert(node, data):
    if node is None:
        return Node(data)
    else:
        if data <= node.data:
            node.left = insert(node.left, data)
        else:
            node.right = insert(node.right, data)
        return node

if __name__ == "__main__":
    root = None
    root = insert(root, 4)
    insert(root, 2)
    insert(root, 1)
    insert(root, 3)
    insert(root, 6)
    insert(root, 5)
    utility.pre = 0
    utility.succ = 0
    utility(root,4)
    print(utility.pre, utility.succ)