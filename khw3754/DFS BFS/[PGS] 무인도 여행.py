from collections import deque


def bfs(maps, x, y):
    q = deque()
    q.append((x, y))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    result = 0

    visited[x][y] = True

    while q:
        x, y = q.popleft()
        result += int(maps[x][y])

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if maps[nx][ny] != 'X' and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True

    return result


visited = []


def solution(maps):
    global visited
    visited = [[False for _ in range(len(maps[0]))] for i in range(len(maps))]

    answer = []

    for x in range(len(maps)):
        for y in range(len(maps[0])):
            if maps[x][y] != 'X' and not visited[x][y]:
                answer.append(bfs(maps, x, y))

    if answer:
        return sorted(answer)
    else:
        return [-1]