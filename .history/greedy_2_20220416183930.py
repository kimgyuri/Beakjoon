N, M = map(int, input().split())
arr = []
max = 0

for i in range(N):
    column = list(map(int, input().split()))
    column.sort()
    arr.append(column)

for i in arr:
    if max < i[0]:
        max = i[0]

print(max)
