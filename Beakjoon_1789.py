N = int(input())

num = 1
count = 0
while N >= num:
    N -= num
    num += 1

print(num-1)