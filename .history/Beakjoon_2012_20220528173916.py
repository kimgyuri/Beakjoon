N = int(input())

expect_score = []
for i in range(N):
    expect_score.append(int(input()))

expect_score.sort()

dissat = 0
for i in range(N):
    dissat += abs(expect_score[i]-(i+1))

print(dissat)
