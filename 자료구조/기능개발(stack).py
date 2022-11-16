def solution(progresses, speeds):
    answer = []
    day = []
    for i in range(len(progresses)):
        target =0
        if (100-progresses[i]) % speeds[i] != 0:
            target = (100-progresses[i]) / speeds[i] +1
        else:
            target = (100-progresses[i]) / speeds[i]
        
        day.append(int(target))
    

    cnt = 1
    pre = day[0]
    tmp = []
    
    print(day)
    for i in range(1,len(day)):
        if pre >= day[i] :
            cnt +=1
            if i == len(day)-1:
                tmp.append(cnt)
        else:
            pre = day[i]
            tmp.append(cnt)
            cnt = 1
            if i == len(day)-1:
                tmp.append(cnt)

    return tmp
