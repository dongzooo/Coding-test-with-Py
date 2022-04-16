def sol1():
  input_data = input()
  row = int(input_data[1])
  column = int(ord(input_data[0]))- int(ord('a')) +1
  
  
  #나이트가 움직일 수 있는 경우의수
  steps = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2), (-2,1),(-2,-1),(-1,2)]
  
  result = 0
  
  for step in steps:
   
    #이동하고자 하는 위치 홧인
    next_row = row+step[0]
    next_col = column + step[1]
      
    if next_row >=1 and next_row <=8 and next_col >=1 and next_col <=8:
      result += 1
  
  print(result)


def sol2(): 
  kn = input()
  #나이트가 움직일 수 있는 경우의수
  steps = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2), (-2,1),(-2,-1),(-1,2)]
  
  col = ['a','b','c','d','e','f','g','h']
  
  result = 0
  
  x, y = int(col.index(kn[0]))+1, int(kn[1])
  
  for step in steps:
    nx ,ny = x,y
    nx += step[0]
    ny += step[1]
    if nx >= 1 and nx <= 8 and ny <= 8 and ny >=1:
      result +=1
  
  print(result)
