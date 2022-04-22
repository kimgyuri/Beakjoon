A, B = map(int, input().split())

count = 1
while A != B:
    tmp = B
    if B%10 == 1:
        B //= 10
        count += 1
    elif B%2 == 0:
        B //= 2
        count += 1
    if tmp == B:
        count = -1
        break

print(count)
    