N = int(input()) # 줄 개수
weights = []

for i in range(N):
    weights.append(int(input()))

weights.sort(reverse=True)

tmp = 0
for i in range(len(weights)):
    weight = weights[i]*(i+1)
    if tmp < weight:
        tmp = weight
    else:
        continue

print(tmp)