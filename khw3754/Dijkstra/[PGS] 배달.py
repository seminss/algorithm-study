from collections import deque

def bfs(towns, K):
    q = deque()
    q.append((1, 0))
    visited = {i: float('inf') for i in range(1, len(towns) + 1)}
    visited[1] = 0

    while q:
        pos, time = q.popleft()
        nexts = towns[pos]
        for nextPos, spend in nexts:
            if time + spend <= K and nextPos != pos and visited[nextPos] > time + spend:
                q.append((nextPos, time + spend))
                visited[nextPos] = time + spend

    return len(list(filter(lambda x: x[1] <= K, visited.items())))


def solution(N, road, K):
    answer = 0

    towns = {n: [] for n in range(1, N + 1)}
    # 마을번호 : [[이어진 마을, 최소 시간], ...] 으로 만듦
    for a, b, c in road:
        fil = list(filter(lambda x: x[0] == b, towns[a]))
        if len(fil) == 0:
            towns[a].append([b, c])
            towns[b].append([a, c])
        else:
            if fil[0][1] > c:
                fil[0][1] = c
                list(filter(lambda x: x[0] == a, towns[b]))[0][1] = c

    return bfs(towns, K)