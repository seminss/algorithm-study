from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0

    onBridge = 0
    time = 1
    onBridgeTime = deque()  # [[무게, 올라간 시간], ..]
    for truck in truck_weights:

        # 지금 다리에 올라갈 수 없으면 올라갈 수 있을 때까지 차를 통과
        while onBridgeTime and (onBridge + truck > weight or bridge_length <= len(onBridgeTime)):
            w, t = onBridgeTime.popleft()
            ##### 여기가 문제
            time = t + bridge_length if time < t + bridge_length else time
            onBridge -= w

        # 차를 진입시킴
        onBridgeTime.append([truck, time])
        onBridge += truck
        time += 1
        print(onBridgeTime)

    return onBridgeTime[-1][1] + bridge_length