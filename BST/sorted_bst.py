from .implementation import Node


def utility(arr, start, end):
    if start > end:
        return 0
    utility(arr, start*2+1 , end)
    print(arr[start])
    utility(arr, start*2+2, end)


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
    st = [4, 2, 5, 1, 3]
    utility(st, 0, len(st)-1)
