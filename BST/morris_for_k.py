class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


def k_morris(root, k):
        count = 0
        current = root
        while current:
            if not current.left:
                count = count + 1
                if count == k:
                    print(current.data)
                current = current.right
            else:
                pre = current.left
                while pre.right and pre.right != current:
                    pre = pre.right
                if not pre.right:
                    pre.right = current
                # breaking links
                if pre.right == current:
                    count = count + 1
                    if count == k:
                        print(pre.right.data)
                    pre.right = None


