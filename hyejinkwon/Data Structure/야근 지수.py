'''
남은 일 **2 더한 값
야근 피로도 최소화 
'''

import heapq

def solution(n, works):
    answer = 0
    max_work_heap = []
    
    if n >= sum(works) :
        return 0
    
    for w in works :
        heapq.heappush(max_work_heap, -1*w)
    
    for _ in range(n) : 
        # heapify 쓰는 것 보다 heappop -> heappush 가 효율성 좋음
        queue = heapq.heappop(max_work_heap) + 1
        heapq.heappush(max_work_heap, queue)
        
    for w in max_work_heap :
        answer += (w**2)    

    return answer