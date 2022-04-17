N, K = map(int, input().split())

count = 0

while int(N) != 1:
    while int(N%K) != 0:
        N -= 1
        count += 1
    N //= K
    count += 1

print(count)