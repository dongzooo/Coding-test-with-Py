n, m = map(int, input().split())

#방문할 위치를 저장할 맵 제작
d = [[0]* m for _ in range(n)]
#캐릭터의 x,y 방향 입력받기
x,y, direction = map(int, input().split())
d[x][y]=1

arr = []
for i in range(n):
  arr.append(list(map(int, input().split())))

# 북 동 남 서 방향 정의
dx = [-1 , 0, 1,0]
dy = [0,1,0,-1]

def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction =3

cnt = 1
turn_time = 0
while True:
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]

  if d[nx][ny] ==0 and arr[nx][ny] ==0:
    d[nx][ny]=1
    x = nx
    y = nx
    cnt += 1
    turn_time = 0
    continue

  else:
    turn_time +=1

  if turn_time ==4 :
    nx = x -dx [direction]
    ny = y- dy[direction]

    if arr[nx][ny] == 0 :
      x =nx
      y= nx
    else :
      break

  turn_time = 0


print(cnt)
  
