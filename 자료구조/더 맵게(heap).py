import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    # heapq.heappush(scoville,2)

    while True :
        a = heapq.heappop(scoville)
        if a >=K :
            break
        if len(scoville) ==0:
            return -1
        b = heapq.heappop(scoville)
        new = a+(b*2)
        heapq.heappush(scoville, new)
        answer +=1
        
    
    return answer
