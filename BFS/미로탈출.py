from collections import deque

n, m = map(int, input().split())

#맵 구성하기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 좌표 이동할 방향 정의 (상, 하, 좌, 우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# bfs 함수
def bfs(x, y):
    # 큐 구현
    queue = deque()
    queue.append((x,y))
    
    # 큐가 비어질 때까지 변경 
    while queue:
        x, y = queue.popleft()
        
        # 현 위치 기준 네 방향 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 예외처리: 맵을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 continue
            if graph[nx][ny] == 0:
                continue
            # 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    # 가장 오른쪽 아래, 최단 거리 return
    return graph[n-1][m-1]

print(bfs(0,0))
