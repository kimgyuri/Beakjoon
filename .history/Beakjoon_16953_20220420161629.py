A, B = map(int, input().split())

count = 0
while A < B:
    if B%10 == 1:
        B = int(str(B).rstrip('1'))
        count += 1
    else:
        B //= 2
        count += 1

if A == B:
    print(count)
else:
    print(-1)
    