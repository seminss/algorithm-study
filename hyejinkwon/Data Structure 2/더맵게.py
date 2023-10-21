'''
가장안매운거 + 그다음 안매운거*2
모든 음식 스코빌 지수 >= K 반복! -> 반복해야하는 최소 횟수구하기
자동 오름차순 -> heapq
'''
import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    
    for s in scoville :
        heapq.heappush(heap,s)    
        
    while heap[0] < K :
        answer += 1
        
        if len(heap) >= 2 :
            v_1 = heapq.heappop(heap)
            v_2 = heapq.heappop(heap)
            heapq.heappush(heap, v_1+v_2*2)
        else :
            if heap[0] >= K : return answer
            else : return -1
    
    return answer