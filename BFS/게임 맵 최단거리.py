from collections import deque

def solution(maps):
    answer = 0
    #상,하,좌,우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    queue = deque()
    queue.append((0,0))
    while queue :
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #out of range
            if nx >= len(maps) or nx < 0 or ny >= len(maps[0]) or ny <0 :
                continue
            
            #벽인 경우
            if maps[nx][ny] == 0 :
                continue
            
            #길인 경우
            if maps[nx][ny] == 1 :
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx,ny))
    
    answer = maps[len(maps)-1][len(maps[0])-1]
    
    
    return answer if answer not in [0,1] else -1
