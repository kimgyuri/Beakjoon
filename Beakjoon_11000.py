import heapq
N = int(input())

schedule = []

for _ in range(N):
    a, b = map(int, input().split())
    schedule.append([a, b])
schedule.sort()

heap = []
heapq.heappush(heap, schedule[0][1])

for i in range(1, N):
    if schedule[i][0] < heap[0]:
        heapq.heappush(heap, schedule[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, schedule[i][1])

print(len(heap))
