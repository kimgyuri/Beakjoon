
N = int(input())
dice = list(map(int, input().split()))
min_dice = [min(dice[0], dice[5]), min(dice[1], dice[4]), min(dice[2], dice[3])]
min_dice.sort()

result = 0

if N == 1:
    dice.sort()
    for i in range(5):
        result += dice[i]
else:
    # 1면, 2면, 3면 최솟값
    min1 = min_dice[0]
    min2 = min_dice[0] + min_dice[1]
    min3 = sum(min_dice)

    # 3면 개수
    cnt3 = 4
    # 2면 개수
    cnt2 = 4 * (N-2) + 4 * (N-1)
    # 1면 개수
    cnt1 = (N-2)**2 + 4 * (N-2) * (N-1)

    result += min3 * cnt3
    result += min2 * cnt2
    result += min1 * cnt1
print(result)
