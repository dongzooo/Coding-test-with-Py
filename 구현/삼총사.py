def solution (number) :
    from itertools import combinations
    ans = 0
    for i in combinations(number,3):
        if sum(i) == 0 :
            ans +=1
    return ans
