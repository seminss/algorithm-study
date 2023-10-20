# 같이 공부하면 각각 공부 전 능력치의 합
# 중복 선발 가능

import heapq

def solution(ability, number):
    answer = 0
    heap = []
    for a in ability :
        heapq.heappush(heap,a)
    
    for _ in range(number) :
        prev_0 = heapq.heappop(heap)
        prev_1 = heapq.heappop(heap)
        
        heapq.heappush(heap, prev_0+prev_1)
        heapq.heappush(heap, prev_0+prev_1)
        
    answer = sum(heap)
    
    return answer