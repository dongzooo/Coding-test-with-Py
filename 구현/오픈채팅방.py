def solution(record):
    answer = []
    dic = {}
    tmp = []
    
    #최종 이름만 알면 된다?
    for i in record :
        if i[0] == 'E':
            el, uid, name = i.split(' ')
            dic[uid] = name
        elif i[0] == 'C':
            el, uid, name = i.split(' ')
            dic[uid] = name
        elif i[0] == 'L':
            continue
    
    for i in record:
        if i[0] == 'E':
            el, uid, name = i.split(' ')
            answer.append(dic[uid]+'님이 들어왔습니다.')
        elif i[0] == 'C':
            continue
        elif i[0] == 'L':
            el, uid = i.split(' ')
            answer.append(dic[uid]+'님이 나갔습니다.')
        
    
    
    return answer
