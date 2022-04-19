n = input().split('-')
list = []

for i in n:
    tmp = 0
    plus = i.split('+')
    for j in plus:
        tmp += int(j)
    list.append(tmp)

for i in range(1, len(list)):
    list[0] -= list[i]

print(list[0])