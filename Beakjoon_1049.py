import heapq

N, M = map(int, input().split())

packages, pieces = [], []
for _ in range(M):
    a, b = map(int, input().split())
    packages.append(a)
    pieces.append(b)

result = 0
while N != 0:
    heap = []
    for package in packages:
        heapq.heappush(heap, package)
    if N >= 6:
        for piece in pieces:
            heapq.heappush(heap, piece*6)
        result += (heap[0]*(N//6))
        N %= 6
    else:
        for piece in pieces:
            heapq.heappush(heap, piece*N)
        result += (heap[0])
        N -= N

print(result)
