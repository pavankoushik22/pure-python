# so far this is a naive method

def kth(root, k):
    stk = []
    while root:
        stk.append(root)
        root = root.left
    while k != 0 :
        temp = stk.pop()
        if k == 1:
            return temp.data
        if temp.right:
            stk.append(temp.right)
            temp = temp.right
            while temp.left:
                stk.append(temp.left)
                temp = temp.left
        k = k-1


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


if __name__ == "__main__":
    root = Node(20)
    root.left = Node(8)
    root.right=Node(22)
    root.left.left = Node(4)
    root.left.right= Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    print(kth(root, 5))
