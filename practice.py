N = int(input())

result = 0
while N > 0:
    if N%5 == 0:
        N %= 5
        result += N//5
    elif N%3 == 0:
        N %= 3
        result += N//3
    else:
        result = -1
        break

print(result)
