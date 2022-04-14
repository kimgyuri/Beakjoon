n = int(input()) # N명
time_arr = [] # 인출 시간
total_time = 0 # 필요한 총 시간

for i in range(n):
    t = int(input())
    time_arr.append(t)

time_arr = time_arr.sort()


while len(time_arr)!=0:
    for i in time_arr:
        total_time += i

    time_arr.pop()