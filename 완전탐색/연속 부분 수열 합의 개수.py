def solution(elements):
    answer = 0
    sumList = []
    tempEl = elements*2

    for i in range(1,len(elements)+1):
        for j in range(len(elements)):
            sumList.append(sum(tempEl[j:j+i]))

    answer = len(set(sumList))
    return answer
