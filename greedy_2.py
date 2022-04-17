N, M = map(int, input().split())
arr = []
max_value = 0

# for i in range(N):
#     column = list(map(int, input().split()))
#     column.sort()
#     arr.append(column)

# for i in arr:
#     if max_value < i[0]:
#         max_value = i[0]

for i in range(N):
    column = list(map(int, input().split()))
    min_value = min(column)
    max_value = max(max_value, min_value)

print(max_value)