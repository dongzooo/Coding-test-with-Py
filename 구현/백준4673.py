array = []
for i in range(1, 10001):
    array.append(i)

# 수열  리스트
newArray = []
m = 0

for i in array:
    iStr = str(i)
    
    # 각 자리의 수를 더함
    for k in range(len(iStr)):
        m += int(iStr[k])
    m += i  # 각 자리의 수를 더한 값에 원래값을 더해줌
    newArray.append(m)  
    m = 0  # m값 초기화

# 셀프 넘버 구하기 (각 리스트를 set로 변환한 뒤 차집합 구하기)
# set로 변환하는 과정에서 중복된 값이 제거된다.
selfnum = set(array) - set(newArray)
array = list(selfnum)
array.sort()  # 오름차순 정렬

for i in array:
    print(i)
