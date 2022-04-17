from collections import deque
N = int(input()) # 회의 수
time_arr = [] # 시간 배열
result = 0 # 회의 최대 개수

for i in range(N):
    time_arr.append(tuple(map(int, input().split())))

result = sorted(result, key=lambda x: x[1])
