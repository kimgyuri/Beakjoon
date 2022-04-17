from collections import deque
N = int(input()) # 회의 수
time_arr = [] # 시간 배열
result = 0 # 회의 최대 개수

for i in range(N):
    time_arr.append(tuple(map(int, input().split())))

time_arr = sorted(time_arr, key=lambda x: (x[1], x[0]))
print(time_arr)

