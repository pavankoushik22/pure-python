def heapify(arr, i):
    index = i
    l = 2*index + 1
    r = 2*index + 2
    if l < len(arr)-1 and arr[l] > arr[index]:
        largest = l

    if r < len(arr)-1 and arr[r] > arr[index]:
        largest = r

    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        heapify(arr, largest)


def heapsort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0)
