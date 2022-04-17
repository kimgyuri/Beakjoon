N, M = map(int, input().split())
arr = []

for i in range(N):
    column = list(map(int, input().split()))
    column.sort()
    arr.append(column)
    