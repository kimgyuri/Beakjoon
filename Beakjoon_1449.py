N, L = map(int, input().split())

water = list(map(int, input().split())) # 전체 물 새는 곳
water.sort(reverse=True) # 뒤에서부터 꺼내기 때문에 reverse

result = 0 # 결과 값
use_tape = L-1 # 사용한 테이프
tmp = water.pop() # 처음 물 새는 곳

while water:
    tmp1 = water.pop() # 그 다음 물 새는 곳
    if tmp1 < (tmp+L): # 처음 물 새는 곳 범위 안에 존재할 경우
        use_tape -= (tmp-tmp1) # 테이프 사용
        if use_tape == 0: # 테이프를 다 사용했을 경우
            result += 1 
            use_tape = L-1 # 결과 값에 1 더해주고 원래 길이로 할당
    else: # 처음 물 새는 곳 범위 안에 존재하지 않는 경우
        tmp = tmp1  # 다음 구간 처음 물 새는 곳으로 할당
        if L == 1 or use_tape != 0: # 가지고 있는 테이프 길이가 1이거나 사용한 테이프 길이가 0이 아닐 때
            use_tape = L-1
            result += 1

if L == 1 or use_tape != 0:
    result += 1

print(result)
