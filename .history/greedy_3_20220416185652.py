N, K = map(int, input().split())

count = 0

while(N != 1):
    while(N%K != 0):
        N -= 1
        count += 1
        print(N)
    N /= K
    count += 1
    print(N)

print(count)