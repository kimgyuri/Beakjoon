import sys
import heapq

N = int(sys.stdin.readline())
min_heap = []

for i in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(min_heap) == 0:
            print(0)
        else:
            print(min_heap[0])
            heapq.heappop(min_heap)
            # print(min_heap)
    else:
        heapq.heappush(min_heap, x)
        # print(min_heap)