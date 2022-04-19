n, m = map(int, input().split())

#2차원 리스트 맵 정보 생성
graph = []
for i in range(N):
    graph.append(list(map(int,input())))

#DFS로 특정 노드 방문후 인접노드까지 방문하기
def dfs(x, y):
    # 맵 벗어나면 종료
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    # 상, 하, 좌, 우 순으로 스택에 push. 방문한 경우 False
    if graph[x][y] == 0:
      #노드 방문처리
        graph[x][y] = 1
        
        #상 하 좌 우 위치 모두 재귀적으로 탐색
        dfs(x-1, y) 
        dfs(x+1, y) 
        dfs(x, y-1) 
        dfs(x, y+1) 
        return True
    return False

#음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
