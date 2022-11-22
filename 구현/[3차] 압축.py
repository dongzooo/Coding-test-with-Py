def solution(msg):
    answer = []
    dic ={}
    for i in range(26):
        dic[chr(65+i)] = i+1
    print(dic)
    #c가 사전에 있으면 pass, c+w가 사전에 없으면 추가하고 그 전에 인덱스를 answer에 넣는다
    w,c = 0,0
    while True:
        c+=1
        if c == len(msg):
            answer.append(dic[msg[w:c]])
            break
            
        if msg[w:c+1] not in dic:
            dic[msg[w:c+1]] = len(dic)+1
            answer.append(dic[msg[w:c]])
            w = c
            
    
    return answer

    
