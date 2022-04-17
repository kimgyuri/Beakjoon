N = int(input()) # 회의 수
time_arr = []
for i in range(N):
    time_arr.append(tuple(map(int, input().split())))

print(time_arr)