import heapq
import sys

left, right = [], []

N = int(sys.stdin.readline())

for i in range(N):
    num  = int(sys.stdin.readline())

    if len(left) == len(right):
        # max_heap
        heapq.heappush(left, (-num, num))
    else:
        # min_heap
        heapq.heappush(right, (num, num))
    
    if right and left[0][1] > right[0][1]:
        left_max_value = heapq.heappop(left)[1]
        right_min_value = heapq.heappop(right)[1]
        heapq.heappush(left,(-right_min_value, right_min_value))
        heapq.heappush(right, (left_max_value, left_max_value))

    print(left[0][1])