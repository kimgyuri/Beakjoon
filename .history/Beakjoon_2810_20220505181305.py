from collections import deque
N = int(input())
seats = deque(list(str(input())))

holder_cnt = 1
people_cnt = 0

while len(seats) > 0:
    tmp = seats.popleft()
    if tmp == 'S':
        people_cnt += 1
        holder_cnt += 1
    else:
        tmp = seats.popleft()
        people_cnt += 2
        holder_cnt += 1
    

if holder_cnt < people_cnt:
    print(holder_cnt)
else:
    print(people_cnt)
