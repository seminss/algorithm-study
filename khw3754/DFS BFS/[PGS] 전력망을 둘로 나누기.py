from collections import deque


def solution(n, wires):
    # 연결 정보 딕셔너리에 저장
    wire_dict = {i: [] for i in range(1, n + 1)}
    for wire in wires:
        wire_dict[wire[0]].append(wire[1])
        wire_dict[wire[1]].append(wire[0])

    # wires 중 하나씩 끊어보면서 비교
    min = n + 1
    for a, b in wires:
        # 끊고
        wire_dict[a].remove(b)
        wire_dict[b].remove(a)

        # 차이 계산
        count = bfs(wire_dict, 1)
        count = abs(count - (n - count))
        if min > count:
            min = count

        # 원상복구
        wire_dict[a].append(b)
        wire_dict[b].append(a)

    return min


# target 노드의 트리에 노드가 몇 개인지 반환하는 함수
def bfs(wires_dict, target):
    visited = [False for _ in range(len(wires_dict) + 1)]
    result = 0

    q = deque()
    q.append(target)
    visited[target] = True
    result += 1

    while q:
        t = q.popleft()
        w_list = wires_dict[t]
        for w in w_list:
            if not visited[w]:
                q.append(w)
                visited[w] = True
                result += 1

    return result