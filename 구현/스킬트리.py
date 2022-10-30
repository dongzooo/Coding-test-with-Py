def solution(skill, skill_trees):
    answer = 0

    for i in skill_trees:
        tmpWord = ''
        for j in i : 
            if j in skill:
                tmpWord += j
        if skill[:len(tmpWord)] == tmpWord:
            answer +=1
    
    return answer
