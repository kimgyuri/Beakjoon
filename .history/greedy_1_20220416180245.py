N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

arr = sorted(arr, reverse=True)
sum = 0
count = 0

while count != M:
    if arr[0] == arr[1]:
        for i in range(M):
            sum += arr[0]
            count += 1
    else:
        for i in range(K):
            sum += arr[0]
            count += 1
        sum += arr[1]
        count += 1


print(sum)