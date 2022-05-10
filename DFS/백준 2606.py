import sys
input = sys.stdin.readline

C = int(input().rstrip())
S = int(input().rstrip())
graph = [[] for _ in range(C + 1)]

for i in range(S):
  node, node2 = map(int, input().split())
  graph[node].append(node2)
  graph[node2].append(node)
  

def dfs():
  visited = []
  stack = [graph[1]]
  cnt = 0

  while stack:
    cur = stack.pop()
    for i in cur:
      if not i in visited:
        visited.append(i)
        stack.append(graph[i])
        cnt += 1

  print(cnt - 1)
  
  
 dfs()
