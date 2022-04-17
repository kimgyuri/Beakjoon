N = int(input()) # 동전종류
K = int(input()) # 가치
coins = [] # 동전 배열
result = 0

for i in range(N):
    coin = int(input())
    coins.append(coin)

while K != 0:
    tmp = coins.pop()
    
    if K >= tmp:
        result += K/tmp
        K = K%tmp
    else:
        continue