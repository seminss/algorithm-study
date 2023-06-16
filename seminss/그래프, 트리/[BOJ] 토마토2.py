import sys
from collections import deque

dx = [1, -1, 0, 0,0,0]
dy = [0, 0, 1, -1,0,0]
dz=[0,0,0,0,1,-1]


def bfs(ripe, qub):
    queue = deque(ripe)
    max_days = 0

    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz=z+dz[i]
            if nx < 0 or ny < 0 or nz<0 or nx >= m or ny >= n or nz>=h:
                continue
            if qub[nz][ny][nx] == 0:
                queue.append((nx, ny,nz))
                qub[nz][ny][nx] = qub[z][y][x] + 1
                max_days = max(max_days, qub[nz][ny][nx] - 1)
    for s in qub:
        for l in s:
            if 0 in l:
                return -1
    return max_days

m, n, h = map(int, sys.stdin.readline().split())
qub = list(list(list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)) for _ in range(h))
ripe = [(j, i,w) for w in range(h) for i in range(n) for j in range(m) if qub[w][i][j] == 1]
ans = bfs(ripe, qub)
print(ans)