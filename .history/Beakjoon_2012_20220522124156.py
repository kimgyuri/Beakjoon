N = int(input())

expect_score = []
for _ in range(N):
    expect_score.append(int(input()))

expect_score.sort()

dissat = 0
for i in range(1, N):
    dissat += (i-expect_score[i-1])

print(dissat)