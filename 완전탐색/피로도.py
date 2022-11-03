from itertools import permutations
def solution(k, dungeons):
    answer = 0
    
    for per in permutations(dungeons, len(dungeons)):
        hp = k
        count = 0 
        for p in per:
            if hp >= p[0] :
                hp -= p[1]
                count += 1
        if answer < count :
            answer = count
    
    
    return answer
