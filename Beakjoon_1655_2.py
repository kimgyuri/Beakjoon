# priority queue
import heapq
import sys

left, right = [], []
N = int(sys.stdin.readline())

for i in range(N):
    num = int(sys.stdin.readline())
    if len(left) == len(right):
        # max_heap
        heapq.heappush(left, (-num, num))
    else:
        # min_heap
        heapq.heappush(right, (num, num))
    
    if right and left[0][1] > right[0][1]:
        left_value = heapq.heappop(left)[1]
        right_value = heapq.heappop(right)[1]
        heapq.heappush(right, (left_value, left_value))
        heapq.heappush(left, (-right_value, right_value))
    
    print(left[0][1])