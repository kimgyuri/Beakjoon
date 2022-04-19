import heapq
N = int(input())
cards = []

for _ in range(N):
    heapq.heappush(cards, int(input()))

result = 0
if len(cards) == 1:
    print(result)
else:
    while len(cards) > 1:
        tmp = heapq.heappop(cards) + heapq.heappop(cards)
        heapq.heappush(cards, tmp)
        result += tmp
    print(result)
