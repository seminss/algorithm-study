#11:30~12:08
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    waiting=deque(truck_weights) #대기중인 트럭
    present_weight=0 #현재 다리 위에 있는 트럭 무게 합
    status=deque() #현재 다리 위에 있는 트럭들
    indiv_time=deque() #각 트럭이 다리에서 얼마나 갔나
    
    while waiting or status:
        if status and indiv_time and indiv_time[0]==bridge_length:
                done=status.popleft()
                present_weight-=done
                indiv_time.popleft()
        for i in range(len(indiv_time)):
            indiv_time[i]+=1
        if waiting and present_weight+waiting[0]<=weight:
            new=waiting.popleft()
            status.append(new)
            indiv_time.append(1)
            present_weight+=new
        answer+=1 #전체 시간 count
    return answer