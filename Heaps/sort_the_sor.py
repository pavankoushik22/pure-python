from heapq import heappush, heapify, heappop


def ksort(arr, k):
    for i in range(len(arr)-k):
        # frame is i and i + k
        heap = heapify(arr[i:i+k+1])
        print(heappop(heap), end=' ')
        heappush(heap, arr[k+i])

