n,m,k = map(int, input().split()) 
data = list(map(int, input().split()))

data.sort()

first = data[n-1] # 가장 큰 수
second = data[n-2] # 두번쨰로 큰 수

count = int(m/(k+1)*k + m%(k+1))

result = first*count + (m-count)*second
print(result)
