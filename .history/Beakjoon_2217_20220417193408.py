N = int(input()) # 줄 개수
W = []

for i in range(N):
    W.append(int(input()))

W.sort()

print(W[0]*N)


