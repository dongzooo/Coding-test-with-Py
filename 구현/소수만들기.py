from itertools import combinations

def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return 0
    return 1
        
def solution(nums):
    answer = 0
    for i in combinations(nums,3):
        answer += isPrime(sum(i))
    

    return answer
