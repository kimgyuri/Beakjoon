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
    x, y = x+y, x+y
    heapq.heappush(heap, x)
    heapq.heappush(heap, y)
    cnt += 1

print(sum(heap))
