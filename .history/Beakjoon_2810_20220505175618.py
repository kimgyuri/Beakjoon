from collections import deque
N = int(input())
seats = deque(list(str(input())))

seat_list = ['*']
holder_cnt = 2
people_cnt = 0

print(seats)
# tmp = ''
# for seat in seats:
#     if seat == 'S':
#         seat_list.append(seat)
#         seat_list.append('*')
#         people_cnt += 1
#     else:
#         if tmp == '':
#             tmp += 'L'
#         elif tmp == 'LL':
            