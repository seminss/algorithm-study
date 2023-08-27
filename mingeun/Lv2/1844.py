''' 2023.5.20
16:08 ~ 16:41
'''
from collections import deque
def solution(maps):
    n, m = len(maps), len(maps[0])
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]# 아래, 오른쪽, 위, 왼쪽
    answer = 0
    q = deque([(0, 0)])
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True
    while q:
        x, y = q.popleft()
        if x == n-1 and y == m-1:
            break
        for i in range(4):
            xn, yn = x + dx[i], y + dy[i]
            if 0<=xn<n and 0<=yn<m and maps[xn][yn] != 0 and not visited[xn][yn]:
                maps[xn][yn] = maps[x][y] + 1
                visited[xn][yn] = True
                q.append((xn, yn))
    if maps[n-1][m-1] == 1 or maps[n-1][m-1] == 0:
        return -1
    return maps[n-1][m-1]
