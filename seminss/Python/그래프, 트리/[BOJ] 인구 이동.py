# 2:40
# bfs 로 연합을 만들고 해당 연합이 이동
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, L, R = map(int, sys.stdin.readline().split())

maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


# visited=0,-1,1 인데 0이면 방문 전, -1이면 연합 x, 1이면 연합 0
def bfs(x, y, visited, maps):
    que = deque([(x, y)])
    population = maps[y][x]
    union_list = [(x, y)]
    visited[y][x] = 1
    while que:
        x, y = que.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if nx >= N or nx < 0 or ny >= N or ny < 0:
                continue
            if visited[ny][nx] == 0 and L <= abs(maps[y][x] - maps[ny][nx]) <= R:
                visited[ny][nx] = 1
                population += maps[ny][nx]
                que.append((nx, ny))
                union_list.append((nx, ny))

    if len(union_list) == 1:
        visited[y][x] = -1
        return 0, []
    return population, union_list


def refresh_maps(maps, avg):
    for x, y in union_list:
        maps[y][x] = avg


days = 0

while True:
    visited = [[0] * N for _ in range(N)]
    move = False
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                population, union_list = bfs(j, i, visited, maps)
                if len(union_list) > 0:
                    move = True
                    refresh_maps(maps, population // len(union_list))
    if not move:
        break
    days += 1

print(days)
