#11:45~
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) #scoville이 heapq가 됐다!
    while scoville[0]<K:
        if len(scoville)==1:
            return -1
        n1=heapq.heappop(scoville)
        n2=heapq.heappop(scoville)
        heapq.heappush(scoville,n1+n2*2)
        answer+=1
    return answer