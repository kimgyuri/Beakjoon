from collections import deque

N = int(input())
house = list(map(int, input().split()))

house.sort()
house = deque(house)

