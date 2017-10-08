# naive trail


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


def a_bst(arr, start, end):
    index = (start+end)//2
    temp = Node(arr[index])
    if start > end:
        return temp
    elif start == end:
        return temp
    else:
        temp.left = a_bst(arr, start, index-1)
        temp.right = a_bst(arr, index+1, end)
        return temp

if __name__ == "__main__":
    a = [1, 2, 3]
    result = a_bst(a, 0, len(a)-1)
    print(result.data)
    print(result.left.data)
    print(result.right.data)
