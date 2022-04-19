T = int(input()) # 테스트 케이스

for i in range(T):
    N = int(input()) # 지원자 수
    arr = []
    for _ in range(N):
        arr.append(tuple(map(int, input().split())))
    arr.sort()
    result = 1
    min_score = arr[0][1]
    for j in range(N):
        score = arr[j][1]
        if score < min_score:
            min_score = score
            result += 1
    print(result)
