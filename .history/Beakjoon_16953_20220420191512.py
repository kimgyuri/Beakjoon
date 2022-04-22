# A, B = map(int, input().split())

# count = 1
# while A != B:
#     tmp = B
#     if B%10 == 1:
#         B //= 10
#         count += 1
#     elif B%2 == 0:
#         B //= 2
#         count += 1
#     if tmp == B:
#         count = -1
#         break

# print(count)

from collection import deque

A, B = map(int, input().split())
deq = deque()
deq.append((A, 1))
count = 0

while (deq):
    n, t = deq.popleft()
    if n > B:
        continue
    if n == B:
        print(t)
        break
    deq.append(int(str(n)+"1"), t+1)
    deq.append(n*2, n+1)
else:
    print(-1)