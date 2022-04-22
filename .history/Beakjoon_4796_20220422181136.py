case = 0
arr = []

while True:
    L, P, V = map(int,input().split())
    arr.append([L, P, V])

    if L == 0 and P == 0 and V == 0:
        break

for i in arr:
    for j in i:
        l, p, v = j[0], j[1], j[2]
        
    tmp1 = v//p
    tmp2 = v%p
    result = l * tmp1 + tmp2

    print("Case ", i, ": ", result)