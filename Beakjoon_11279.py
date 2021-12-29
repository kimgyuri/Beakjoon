import sys
import heapq

N = int(sys.stdin.readline())
max_heap = []

for i in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(max_heap) == 0:
            print(0)
        else:
            print(max_heap[0][1])
            heapq.heappop(max_heap)
    else:
        heapq.heappush(max_heap, (-x, x))