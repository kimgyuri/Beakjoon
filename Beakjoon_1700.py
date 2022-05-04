from collections import deque



N, K = map(int, input().split()) # 구멍 개수, 사용 순서
use = deque(list(map(int, input().split())))
plugs = []
count = {}
result = 0

for _ in range(N):
    tmp1 = use.popleft()
    plugs.append(tmp1)
    count[tmp1] = 0

while use:
    tmp2 = use.popleft()
    if tmp2 not in plugs:
        if len(use) == 0:
            result += 1
        else:
            for i in plugs:
                for j in use:
                    if i == j:
                        count[i] += 1
            s_count = sorted(count.items(), key=lambda x:x[1])
            tmp3 = s_count[0][0]
            plugs.remove(tmp3)
            plugs.append(tmp2)
            result += 1
print(result)