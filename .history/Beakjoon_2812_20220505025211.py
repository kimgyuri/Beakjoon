N, K = map(int, input().split())

num = str(input())
result = []
count = K
for i in range(N):
    while len(result) > 0 and count > 0:
        if int(num[i]) > int(result[-1]):
            result.pop()
            count -= 1
        else:
            break
    result.append(num[i])

rersult = ''.join(result)
print(result)