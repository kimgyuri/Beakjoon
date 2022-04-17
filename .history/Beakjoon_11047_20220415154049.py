N, K = map(int, input().split()) # 동전종류, 가치
coins = [] # 동전 배열
result = 0

for i in range(N):
    coins.append(int(input()))

while K != 0:
    tmp = coins.pop()
    
    if K >= tmp:
        result += K/tmp
        K = K%tmp
    else:
        continue

print(result)