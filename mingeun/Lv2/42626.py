''' 2023.5.9
22:54 ~ 23:09
'''
from heapq import heappush
from heapq import heappop
def solution(scoville, K):
    heap = []
    for s in scoville:
        heappush(heap, s)
    answer = 0
    while True:
        food = heappop(heap)
        if len(heap) < 1 and food < K:
            return -1
        elif food >= K:
            return answer
        else:
            blended = food + 2*heappop(heap)
            heappush(heap, blended)
            answer +=1 
