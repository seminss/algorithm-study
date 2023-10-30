import sys
from collections import deque

N, M, T = map(int, sys.stdin.readline().split())
castle = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, visited, castle):
    que = deque([(x, y)])
    visited[y][x] = 1
    gram = float('inf')

    while que:
        x, y = que.popleft()

        if x == M - 1 and y == N - 1:  # 그람 없이 일단 도착
            return min(visited[y][x] - 1, gram)  # 그람이 있다면 그람 있을 때랑 없을 때 더 최소값
        if castle[y][x] == 2:
            gram = (visited[y][x] - 1) + (N - 1 - y) + (M - 1 - x)
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
            if not visited[ny][nx] and (castle[ny][nx] == 0 or castle[ny][nx] == 2):
                visited[ny][nx] = visited[y][x] + 1
                que.append((nx, ny))
    return gram


visited = [[0]*M for _ in range(N)]
result = bfs(0, 0, visited, castle)

if result>T:
    print('Fail')
else:
    print(resu답lt)
이
# 칼을 찾은 경우, 찾지 않고 그냥 간 경우를 나눠 계산하고, 두개를 비교하는 로직이 어려웠습니다.