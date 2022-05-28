R, C = map(int, input().split())

maps = []
for _ in range(R):
    maps.append(list(input()))

dirs=[(-1, 1), (0, 1), (1, 1)] # 우상향, 직진, 좌하향
end_line = C-1

def pipeline(y:int, x: int) -> bool: # 이 함수가 반환하는 자료형은 bool
    # 현 위치에 파이프 생성
    maps[y][x] = 'x'
    # 만약 원웅이 빵집에 도달했다면 True 리턴
    if x == end_line: 
        return True

    for dy, dx in dirs:
        ny, nx = y+dy, x+dx
        # 다음 위치에 파이프 생성 가능한지 확인
        # ny와 nx가 맵 안에 위치하고, '.'일 때 True 리턴
        if 0 <= ny < R and 0 <= nx < C and maps[ny][nx] == '.':
            # 끝까지 설치가 가능하다면
            if pipeline(ny, nx):
                return True
    # 전부 조건이 안되면 False 리턴
    return False

result = 0
for y in range(R):
    if pipeline(y, 0):
        result += 1

print(result)