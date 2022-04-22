A, B = map(int, input().split())

while A < B:
    if B%10 == 1:
        B = int(str(B).rstrip('1'))
    else:
        B //= 2
    