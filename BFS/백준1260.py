visited_bfs = [0] * (n+1)
from collections import deque
def bfs(v):
    visited_bfs[v] = 1                         # 방문처리
    queue = deque()
    queue.append(v)                            # 큐에 노드 삽입
    while queue:                               # 큐에 노드가 없을때까지 반복
        node = queue.popleft()                 # 큐에서 빼주기
        print(node,end=' ')
        for i in range(n+1):
            if visited_bfs[i] == 0 and graph[i][node]: # 방문했었는지, 그리고 간선이 있는지 확인
                queue.append(i)                        # 큐에 노드 삽입
                visited_bfs[i] = 1                     # 방문처리
print()
bfs(v)
