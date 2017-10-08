class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


def build(inorder, levelorder, instrt, inend):
    if instrt > inend:
        return None
    node = Node(levelorder[build.preindex])
    if instrt == inend:
        return node
    inIndex = inorder.index(node.data)
    temp1 = levelorder
    node.left = build(inorder, levelorder)