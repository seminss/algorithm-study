# 모든음식의 스코빌 지수를 K이상으로
# 스코빌 가장 낮은 음식 + 두번째로 낮은음식*2 = 새로운음식
# 모든 음식의 스코빌 지수가 K이상일때까지 반복
# 섞어야 하는 최소 횟수는 ?

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)      # heap정렬 nlogn
    
    while scoville[0] < K :
        if len(scoville) >= 2 :
            s1 = heapq.heappop(scoville) # 가장 작은 수 pop
            s2 = heapq.heappop(scoville)
        
            new = s1 + s2*2
            heapq.heappush(scoville, new)
            answer += 1
            
        if len(scoville) <= 1 and scoville[0] < K :
            return -1
        
    return answer