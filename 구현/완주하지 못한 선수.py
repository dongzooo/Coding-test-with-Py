def solution(participant, completion):
    answer = ''
    completion.sort()
    participant.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i] :
            answer =  participant[i]
            return participant[i]
        else :
             print(i)
            
    return participant[-1]
