A, B = map(int, input().split())

count = 1
while A < B:
    if B%10 == 1:
        B = int(str(B).rstrip('1'))
        count += 1
    elif B%2 == 0:
        B //= 2
        count += 1

if A == B:
    print(count)
else:
    print(-1)
    