#둘레는 brown + 4이다, 가로 >= 세로
# w>=h , 2w+2h = brown +4, brown + yellow = 넓이
# 넓이/가로 = 세로
def solution(brown, yellow):
    answer = []
    for h in range(brown//2):
        for w in range(h,brown//2+1):
            if w >= h :
                if w*h == (brown + yellow)and 2*w+2*h == brown +4 :
                    answer = [w,h]
                    return answer
                    
    return answer   
    
    
        
    
