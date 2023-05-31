from collections import deque

def bfs(maps):
    q = deque()
    q.append((0, 0))

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if maps[nx][ny] == 1:
                    maps[nx][ny] += maps[x][y]
                    q.append((nx, ny))


def solution(maps):
    bfs(maps)
    answer = maps[-1][-1] if maps[-1][-1] != 1 else -1
    return answer