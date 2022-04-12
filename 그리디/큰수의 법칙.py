# 단순 for문
def sol1():
  n,m,k = map(int, input().split())

  data = list(map(int, input().split()))
  result = 0

  data.sort()
  first = data[-1]
  second = data[-2]

  while True :
    for i in range(k):
      if m==0 :
        break
      result += first
      m -= 1
    if m==0 :
        break   
    result += second
    m -=1

  print(result)
  
 # 수열 활용
def sol2():
  n,m,k = map(int, input().split()) 
  data = list(map(int, input().split()))

  data.sort()

  first = data[n-1] # 가장 큰 수
  second = data[n-2] # 두번쨰로 큰 수

  count = int(m/(k+1)*k + m%(k+1))

  result = first*count + (m-count)*second
  print(result)
