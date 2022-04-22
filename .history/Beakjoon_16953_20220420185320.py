A, B = map(int, input().split())

count = 1
while A < B:
    if B%10 == 1:
        B //= 10
        count += 1
    else:
        B //= 2
        count += 1

if A == B:
    print(count)
else:
    print(-1)
    