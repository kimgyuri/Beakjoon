import heapq
N, K = map(int, input().split()) # 보석개수, 가방개수

jewelry = [] # 보석 배열 
for _ in range(N):
    jewelry.append(tuple(map(int, input().split())))

bags = [] # 가방 배열
for _ in range(K):
    bags.append(int(input()))

print(jewelry)
print(bags)


