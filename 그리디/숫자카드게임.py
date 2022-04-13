#각 행중에서 가장 낮은 카드를 뽑는 사람둥 가장 큰수를 뽑으면 승리
#for문으로 최소겂구하기보다는 min메서드로 해결해보자
n ,m = map(int , input().split())

result = 0

for i in range(n):
  data = list(map(int, input().split()))

  minValue = min(data)
  result = max(result, min)

print(result)
