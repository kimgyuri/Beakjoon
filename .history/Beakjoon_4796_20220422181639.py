case = 0
arr = []

while True:
    L, P, V = map(int,input().split())
    arr.append([L, P, V])

    if L == 0 and P == 0 and V == 0:
        break

print(arr)
for i in len(arr)-1:
    l, p, v = arr[i][0], arr[i][1], arr[i][2]
    tmp1 = v//p
    tmp2 = v%p
    result = l * tmp1 + tmp2

    print("Case ", i, ": ", result)