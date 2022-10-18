def solution(n, lost, reserve):
    reserveStu = set(reserve) - set(lost)
    lostStu = set(lost) - set(reserve)
    answer = n - len(lostStu)
    
    for i in lostStu:
        if i-1 in reserveStu:
            reserveStu.remove(i-1)
            answer += 1
        elif i+1 in reserveStu:
            reserveStu.remove(i+1)
            answer += 1
    return answer
