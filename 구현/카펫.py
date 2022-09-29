def solution(brown, yellow):
    # [가로,세로]
    answer = []
    total = brown+yellow
    for b in range(1,total+1):
        a = total/b
        if a >= b:
            if 2*a + 2*b -4 == brown:
                return [a,b]
    return answer
