N = int(input()) # 도시 개수
D = list(map(int, input().split()))
C = list(map(int, input().split()))

C.pop() # 가장 마지막 비용은 필요 없으므로 제거

result = 0
min_cost = C[0]

for i in range(len(C)):
    if C[i] < min_cost:
        min_cost = C[i]
    result += min_cost * D[i] 

print(result)
