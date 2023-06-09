# 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 ?
# 최대 bridge_length대 올라갈 수 있고 weight이하까지 견디기 가능 
# 다리에 완전히 오르지 않은 트럭 무게는 무시

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    wating = deque(truck_weights)
    riding = deque([0] * bridge_length) # 다리를 건너는 트럭
    total = 0 
    
    while riding :
        answer += 1
        total -= riding.popleft()
        
        if wating :            
            if total + wating[0] <= weight:
                w = wating.popleft()
                total += w
                riding.append(w)
            else : # 탑승하지 못하는 트럭무게라면
                riding.append(0) # 0 추가 
        
    return answer