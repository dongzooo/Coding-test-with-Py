from collections import deque

n, k = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
target_s, target_x, target_y = map(int, input().split())

data = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            # 바이러스의 종류(번호), 시간, x위치, y위치 삽입
            data.append((graph[i][j], 0, i, j))

# 정렬 이후에 큐로 옮기기 (낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q = deque(data)

dx = [-1, 0, 1, 0]  # 위 오른쪽 아래 왼쪽
dy = [0, 1, 0, -1]  # 위 오른쪽 아래 왼쪽

# 너비 우선 탐색(BFS) 진행
while q:
    virus, s, x, y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if s == target_s:
        break
    # 현재 노드에서 주변 4가지 위치를 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny))

print(graph[target_x - 1][target_y - 1])
