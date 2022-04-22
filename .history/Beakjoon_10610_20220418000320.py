N = str(input())
sum = 0
arr = []

if "0" not in N:
    print(-1)
else:
    for i in N:
        sum += int(i)
        arr.append(int(i))
    if sum%3 != 0:
        print(-1)
    else:
        result = ""
        arr.sort(reverse=True)
        for i in arr:
            result += str(i)
        print(int(result))
