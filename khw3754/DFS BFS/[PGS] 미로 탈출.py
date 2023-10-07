from collections import deque


def bfs(map, start, end):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visited = [[False for _ in range(len(map[0]))] for _ in range(len(map))]
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = True

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= ny < len(map) and 0 <= nx < len(map[0]) and map[ny][nx] != 0 and not visited[ny][nx]:
                map[ny][nx] += map[y][x]
                q.append((ny, nx))
                visited[ny][nx] = True


def solution(maps):
    answer = 0

    # 시작 지점, 출구, 레버를 찾음
    start = [-1, -1]
    end = [-1, -1]
    lever = [-1, -1]
    found = 0
    for i, line in enumerate(maps):
        for j, room in enumerate(line):
            if room == "S":
                start = [i, j]
                found += 1
            elif room == "E":
                end = [i, j]
                found += 1
            elif room == "L":
                lever = [i, j]
                found += 1
            if found == 3:
                break
        if found == 3:
            break

    # 0, 1로 이루어진 map을 만듦
    # realMap = []
    mapForLever = []
    mapForExit = []
    for line in maps:
        tmp = []
        for room in line:
            if room == "X":
                tmp.append(0)
            else:
                tmp.append(1)
        # realMap.append(tmp)
        mapForLever.append(tmp)
        mapForExit.append(tmp[::])

    # 레버까지의 최단 거리를 구함
    bfs(mapForLever, start, lever)
    if mapForLever[lever[0]][lever[1]] == 1:
        return -1
    answer += mapForLever[lever[0]][lever[1]] - 1

    # 레버에서 출구까지 최단 거리를 구함
    bfs(mapForExit, lever, end)
    if mapForExit[end[0]][end[1]] == 1:
        return -1
    answer += mapForExit[end[0]][end[1]] - 1

    return answer