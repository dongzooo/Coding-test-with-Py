n,k= map(int,input().split())

result = 0

while True:
  #나누어 지는 수로 만들기
  target = (n//k)*k
  result += (n-target)
  n = target
  # 더이상 못나눌 때 종료
  if n<k:
    break
  #k로 만들기
  result += 1
  n//=k

#1만 남기고 빼는 횟수
result += (n-1)
print(result)
   
