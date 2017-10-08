class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


def build(inorder, preorder, instrt, inend):
    if instrt > inend:
        return None
    node = Node(preorder[build.preindex])
    build.preindex += 1
    if instrt == inend:
        return node
    inIndex = inorder.index(node.data)
    node.left = build(inorder, preorder, instrt, inIndex-1)
    node.right = build(inorder, preorder, inIndex+1,inend)

    return node


build.preindex = 0


if __name__ == "__main__":
    root = build(['d', 'b', 'e', 'a', 'f', 'c'], ['a', 'b', 'd', 'e', 'c', 'f'], 0, 5)
    print(root.data)
    print(root.left.data)
    print(root.right.data)