from collections import deque
N = int(input()) # 회의 수
time_arr = [] # 시간 배열
result = 0 # 회의 최대 개수

for i in range(N):
    time_arr.append(tuple(map(int, input().split())))

time_arr = sorted(time_arr, key=lambda x: x[1])
tmp = 0

for i in time_arr:
    start_time = i[0]
    finish_time = i[1]

    if start_time >= tmp:
        result += 1
        tmp = finish_time

print(result)

