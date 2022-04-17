N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

arr = arr.sort()
count = 0
sum = 0

while count != M:
    tmp = arr.pop()
    for i in range(K):
        sum += tmp
    count += 1

print(sum)