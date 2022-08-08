N, M, V = map(int, input().split()) # 정점 개수, 간선 개수, 탐색 시작할 정점 번호

visited = [0] *  (N + 1) # 방문한 곳 체크할 배열

matrix = [[0] * (N + 1) for _ in range(N+1)] # 0으로 초기화 한 배열

# 간선에 따른 1 삽입
for i in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1 # 양방향이므로

def dfs(V):
    # 방문한 곳에 1 넣기
    visited[V] = 1
    print(V, end=' ')

    for i in range(1, N+1):
        if(visited[i] == 0 and matrix[V][i] == 1):
            dfs(i)

def bfs(V):
    # 방문해야 할 곳을 순서대로 넣은 큐
    queue = [V]

    # dfs를 완료한 visited 배열에서 0으로 체크
    visited[V] = 0

    # 큐 안에 데이터가 없을 때까지
    while queue:
        V = queue.pop()
        print(V, end=' ')
        for i in range(1, N+1):
            if(visited[i] == 1 and matrix[V][i] == 1):
                queue.append(i)
                visited[i] = 0

dfs(V)
print()
bfs(V)
