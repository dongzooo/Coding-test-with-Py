def solution(dirs):
    command = {'U':(0,1),'D':(0,-1),'R':(1,0),'L':(-1,0)}
    answer = set()
    cur_x, cur_y = 0,0
    
    for i in dirs:
        next_x, next_y = cur_x + command[i][0] ,cur_y+ command[i][1]
        if -5 <= next_x <= 5 and -5 <= next_y <= 5 :
            answer.add((next_x, next_y, cur_x, cur_y))
            answer.add((cur_x, cur_y, next_x, next_y))
            cur_x, cur_y = next_x, next_y
            

    return len(answer)//2
