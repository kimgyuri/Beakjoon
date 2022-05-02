N = int(input())

numbers = list(map(int, input().split()))
numbers.sort()

sum_num = 0
for i in range(N):
    if sum_num +1 >= numbers[i]:
        sum_num += numbers[i]
    else:
        break
print(sum_num + 1)