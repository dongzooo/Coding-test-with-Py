def solution(people, limit):
    answer = 0
    people.sort()
    i = 0
    j = len(people)-1
    while i<=j:
        if people[i] + people[j] <= limit:
            answer += 1
            i+=1
        elif people[i] + people[j] > limit:
            answer += 1
            j-=1
            continue
        j-=1           
    
    return answer
