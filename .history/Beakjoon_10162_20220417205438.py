T = int(input()) # 초

countA = 0
countB = 0
countC = 0
result = 0

while T != 0:
    if T >= 300:
        T %= 300
        countA += 1
    elif T >= 60:
        T %= 60
        countB += 1
    elif T >= 10:
        T %= 10
        countB += 1
    elif T >= 0:
        result = -1
        break

if result == -1:
    print(result)
else:
    print(countA+" "+countB+" "+countC)