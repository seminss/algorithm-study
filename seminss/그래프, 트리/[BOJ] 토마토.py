import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(ripe, sq):
    queue = deque(ripe)
    max_days = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if sq[ny][nx] == 0:
                queue.append((nx, ny))
                sq[ny][nx] = sq[y][x] + 1
                max_days = max(max_days, sq[ny][nx] - 1)

    if any(0 in l for l in sq):
        return -1
    else:
        return max_days

m, n = map(int, sys.stdin.readline().split())
sq = list(list(map(int, sys.stdin.readline().strip().split())) for _ in range(n))
ripe = [(j, i) for i in range(n) for j in range(m) if sq[i][j] == 1]
ans = bfs(ripe, sq)
print(ans)

#시간 단축 : deque 쓰기, 리스트 컴프리헨션, max_days 바로바로 저장