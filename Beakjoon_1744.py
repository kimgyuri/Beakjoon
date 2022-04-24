N = int(input())

positive = [] # 양수
negative = [] # 음수
zero = 0 # 0의 개수

for _ in range(N):
    x = int(input())
    if x < 0:
        negative.append(x)
    elif x == 0:
        zero += 1
    else:
        positive.append(x)

positive.sort()
negative.sort(reverse=True) # 음수의 경우 배열을 뒤집어서 끝부터 꺼내서 곱해야 최대가 됨
result = 0

while negative:
    if len(negative)%2 == 0: # 2개씩 짝지을 수 있을 때
        A = negative.pop()
        B = negative.pop()
        result += A*B
    else:
        if len(negative) == 1: # 1개가 남는 경우
            if zero == 0: # 0이 없는 경우 음수를 바로 더해준다.
                result += negative.pop() 
            else: # 0이 있는 경우 0을 곱해 없애주고 0의 개수를 1개 줄인다.
                zero -= 1
            break
        else:
            A = negative.pop()
            B = negative.pop()
            result += A*B 

while positive:
    if len(positive)%2 == 0: # 2개씩 짝지을 수 있을 때
        A = positive.pop()
        B = positive.pop()
        if A == 1 or B == 1: # 1이 존재할 때
            result += (A+B) # 바로 더해준다.
        else:
            result += A*B
    else:
        if len(positive) == 1:
            result += positive.pop()
        else:
            A = positive.pop()
            B = positive.pop()
            if A == 1 or B == 1:
                result += (A+B)
            else:
                result += A*B

print(result)