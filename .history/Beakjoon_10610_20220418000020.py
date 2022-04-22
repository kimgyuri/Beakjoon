N = int(input())
sum = 0
arr = []

if 0 not in N:
    print(-1)
else:
    for i in N:
        sum += i
        arr.append(i)
    if sum%3 != 0:
        print(-1)
    else:
        result = ""
        arr.sort(reverse=True)
        for i in arr:
            result += i
        print(result)
