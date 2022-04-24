import heapq
N, K = map(int, input().split()) # 보석개수, 가방개수

jewelry = [tuple(map(int, input().split())) for _ in range(N)] # 보석 배열 
jewelry.sort()

bags = [int(input()) for _ in range(K)]# 가방 배열
bags.sort()

result = 0
heap = []

for i in bags:
    while jewelry and i >= jewelry[0][0]: # jewelry[0][0] : 무게가 가장 작은 원소
        heapq.heappush(heap, -jewelry[0][1]) # jewelry[0][1] : 무제가 가장 작은 원소의 가치 
        heapq.heappop(jewelry)
    
    if heap: # heap이 비어있지 않다면
        result += heapq.heappop(heap) # 가장 큰 값을 더해줌
    elif not jewelry: # jewelry가 비어있다면
        break

print(-result)
        