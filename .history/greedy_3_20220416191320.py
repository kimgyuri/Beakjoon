N, K = map(int, input().split())

count = 0

while True:
    while(N%K != 0):
        N -= 1
        count += 1
    if N == 1:
        break
    else:
        N /= K
        count += 1

print(count)