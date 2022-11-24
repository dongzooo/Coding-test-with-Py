import math
def solution(fees, records):
    answer = []
    l = []
    dict = {}  #결과값을 합산할 차량 딕셔너리
    
    #이중 리스트로 만들어서 차번호 순서로 정렬한다 
    for r in records:
        time, num, io = r.split(' ')
        l.append([num,time,io])
        dict[num] = 0
    l = sorted(l)     
    
    #0을 기준으로 그전값과 비교해서 총 시간 구하기
    preNum, preTime, preIo = l[0][0], l[0][1], l[0][2]
    preh,prem = preTime.split(':')
    preTime = int(preh)*60+int(prem) 
    
    #길이가 1일 떄
    if len(l) == 1:
        if (23*60+59)-preTime <= fees[0]:
            answer.append(fees[1])
        else :
            fee = fees[1] + math.ceil(((23*60+59)-preTime-fees[0])/fees[2])*fees[3]
            answer.append(fee)
        return answer
        
    for i in range(1,len(l)):
        num, time, io = l[i][0], l[i][1], l[i][2]
        h,m = time.split(':')
        time = int(h)*60+int(m)
        
        #11:59분에 출차한 경우 
        if (io == 'IN' and i == len(l)-1) or (io == 'IN' and num != l[i+1][0]):
            #print(i,'2',(23*60+59),'-',time,':',(23*60+59)-preTime)
            dict[num] += (23*60+59)-time
            
        elif preNum == num and preIo == 'IN' and io =='OUT':
            #print(i,'2',time,'-',preTime,':',time-preTime)
            dict[num] += time-preTime

        preNum, preTime, preIo = num, time, io
    
    
    #기본 시간(분)	기본 요금(원)	단위 시간(분)	단위 요금(원)
    #시간을 합쳐서 계산하려 출력한다.
    dict = sorted(dict.items())
    for k,v in dict:
        #print(k,v)
        if v <= fees[0]:
            answer.append(fees[1])
            continue
        
        fee = fees[1] + math.ceil((v-fees[0])/fees[2])*fees[3]
        answer.append(fee)
    
    return answer
