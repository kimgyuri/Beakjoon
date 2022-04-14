n = int(input()) # N명
time_arr = list(map(int, input().split())) # 사람 당 인출 시간
total_time = 0 # 필요한 총 시간

time_arr = time_arr.sort()

print(time_arr)
# while len(time_arr)!=0:
#     for i in time_arr:
#         total_time += i

#     time_arr.pop()

# print(total_time)