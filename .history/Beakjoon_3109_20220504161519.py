R, C = map(int, input().split())

pipe = []
for _ in range(R):
    for _ in range(C):
        pipe.append(list(map(str, input().split())))