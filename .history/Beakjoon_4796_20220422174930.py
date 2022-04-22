case = 0
L = -1
P = -1
V = -1
while L != 0 and P != 0 and V != 0:
    case += 1
    L, P, V = map(int, input().split())
    tmp1 = V/P
    tmp2 = V%P
    result = L*tmp1 + tmp2

    print("Case ", case, ": ", result)