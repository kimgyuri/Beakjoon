S = str(input())
T = str(input())

result = 1
while S != T:
    if len(T) == 0:
        result = 0
        break
    else:
        tmp = T[-1]
        if tmp == 'A':
            # A 제거
            T = T[:len(T)-1] 
            continue
        else:
            # B 제거 후 뒤집기
            T = T[:len(T)-1]
            T = T[::-1]

print(result)