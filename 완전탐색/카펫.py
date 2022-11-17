def solution(brown, yellow):
    answer = []
    #넓이 = brown + yellow = w*h
    #       w = (brown + yellow)/h
    #둘레 = brown+4 = 2w+2h
    #w >= h
    for h in range(1,brown//2):
        w = (brown + yellow)/h
        if w >= h :
            if brown+4 == 2*(w+h) :
                answer = [w,h]
                break
    
    return answer
