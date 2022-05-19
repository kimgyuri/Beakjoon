from collections import deque

N = int(input())
house = list(map(int, input().split()))

house.sort()
house = deque(house)

# 양 끝에 위치한 집
right = house[-1]
left = house[0]
mid = (left + right)//2

print(mid)