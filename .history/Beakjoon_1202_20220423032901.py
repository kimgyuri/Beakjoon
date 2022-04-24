from calendar import c
from collections import deque
N, K = map(int, input().split()) # 보석개수, 가방개수

jewelry = []# 보석 배열 
for _ in range(N):
    jewelry.append(tuple(map(int, input().split())))
jewelry.sort()
deq = deque(jewelry)

bags = [] # 가방 배열
for _ in range(K):
    bags.append(int(input()))
bags.sort()

result = 0
while len(bags) != 0:
    tmp = bags.pop()
    for i in deq:
        if i[0] < tmp:
            result += i[1]
            break

print(result)