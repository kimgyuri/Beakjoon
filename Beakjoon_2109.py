import heapq
n = int(input())

school = {} 

# 1. 딕셔너리를 이용해 데이터 매핑
# key: 일 수, value: 강연료
for _ in range(n):
    tmp = list(map(int, input().split()))

    if tmp[1] not in school:
        school[tmp[1]] = [tmp[0]]
    else:
        school[tmp[1]].append(tmp[0])

# 딕셔너리 key를 중심으로 정렬
school = dict(sorted(school.items()))

# 최소힙을 이용해 일 수에 맞춰 강연료가 가장 작은 것을 제거
total_p = []
for k, v in school.items():
    for i in range(len(v)):
        heapq.heappush(total_p, v[i])

    while len(total_p) > k:
        heapq.heappop(total_p)

print(sum(total_p))
