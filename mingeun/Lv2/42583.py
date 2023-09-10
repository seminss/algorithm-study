'''2023.6.8
15:46 ~ 16:29
'''
from collections import deque


def solution(bridge_length, weight, truck_weights):
    """
    시간이 지남에 따라
    조건이 만족될 경우 다리 위에 트럭을 하나씩 올린다.
    1초에 1씩 이동하고 다리의 길이는 bridge_length
    조건
    - len(on_bridge) < bridge_length
    - weight_on_bridge + truck_weights[next_id] <= weight
    종료 조건
    - len(on_bridge) == 0
    - next_id == len(truck_weights)
    """
    on_bridge = deque([]) # 트럭 id 저장
    next_id = 0
    elapsed_time = 0
    weight_on_bridge = 0
    spent_time = [0] * (len(truck_weights))
    
    while True:
        if len(on_bridge) == 0 and next_id == len(truck_weights):
            break
        # 3초가 된 트럭 제거
        while (len(on_bridge) > 0 and spent_time[on_bridge[0]] ==bridge_length):
            i = on_bridge.popleft()
            weight_on_bridge -= truck_weights[i]
        # 가능하다면 트럭 진입
        if next_id < len(truck_weights) \
            and len(on_bridge) < bridge_length \
            and weight_on_bridge + truck_weights[next_id] <= weight:
            on_bridge.append(next_id)
            weight_on_bridge += truck_weights[next_id]
            next_id += 1
        # 다리 위의 트럭들의 운행 시간 + 1
        for i in on_bridge:
            spent_time[i] += 1
        elapsed_time += 1
        # debugging
        # b = [truck_weights[i] for i in on_bridge]
        # print(f'경과 시간: {elapsed_time} 다리 위: {b} 다음 트럭: {next_id}')
        
    return elapsed_time
