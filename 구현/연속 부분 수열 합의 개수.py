def solution(elements):
    answer = 0
    sumList = []
    element = elements*2
    
    for i in range(1,len(elements)+1):
        for j in range(0,len(elements)):
            sumList.append(sum(element[j:j+i]))
    answer =len(set(sumList))
    return answer
