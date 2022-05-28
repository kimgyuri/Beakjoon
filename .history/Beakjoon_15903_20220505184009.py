import heapq
n,m = map(int, input().split())
cards = list(map(int, input().split()))

# 최소힙
heap = []
for i in range(n):
    heapq.heappush(heap, i)
cnt = 0
while m > cnt:
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    print(x, y)
    new_x, new_y = x+y, x+y
    print(new_x, new_y)
    heapq.heappush(heap, new_x)
    heapq.heappush(heap, new_y)
    cnt += 1

print(sum(heap))
