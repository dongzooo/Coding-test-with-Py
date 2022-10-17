def solution(N, stages):
    dict = {}
    answer = []
    len_user = len(stages)
    
    for i in range(1,N+1):
        if len_user != 0:  
            cnt = stages.count(i)
            dict[i] = cnt/len_user
            len_user -= cnt

        else :
            dict[i]=0
    
    answer = sorted(dict, key=lambda x : dict[x], reverse=True)
    
    return answer
