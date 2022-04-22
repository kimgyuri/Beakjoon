A, B = map(int, input().split())

count = 1
while A != B:
    if B%10 == 1:
        B //= 10
        count += 1
    elif B%2 == 0:
        B //= 2
        count += 1
    if A > B:
        count = -1
        break

print(count)
    