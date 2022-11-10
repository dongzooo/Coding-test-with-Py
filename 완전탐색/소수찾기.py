from itertools import permutations

def isPrime(n):
    if n < 2 :
        return 0
    for i in range(2,n):
        if n%i == 0 :
            return 0
    return 1

def solution(numbers):
    answer=0
    nList = set()
    
    for i in range(1, len(numbers)+1):
        for p in permutations(numbers, i):
            nList.add(int(''.join(p)))
            
    for i in nList :
        answer += isPrime(i)
            
    return answer
