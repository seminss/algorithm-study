# 11:05~
import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n = int(sys.stdin.readline())

shark_map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dist_map = [[0] * n for _ in range(n)]
gauge = 0
baby_size = 2
answer = 0


def bfs(x, y, dist_map, shark_map):
    que = deque([(x, y)])
    can_eat = []
    global gauge
    global baby_size
    while que:
        x, y = que.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if dist_map[ny][nx] == 0:
                dist_map[ny][nx] = dist_map[y][x] + 1
                if shark_map[ny][nx] == 0 or shark_map[ny][nx] == baby_size:
                    que.append((nx, ny))
                elif 0 < shark_map[ny][nx] < baby_size:
                    can_eat.append((nx, ny, dist_map[ny][nx]))
                    continue

    if len(can_eat) == 0:
        return [None, None, -1]

    can_eat.sort(key=lambda s: (s[2], s[1], s[0]))  # 거리 가까운 게 1빠, 그다음 y,x 정렬
    shark = can_eat[0]
    shark_map[shark[1]][shark[0]] = 0  # 먹어 치움!
    gauge += 1

    if baby_size == gauge:
        baby_size += 1
        gauge = 0

    return shark


for i in range(n):
    for j in range(n):
        if shark_map[i][j] == 9:
            x = j
            y = i
            shark_map[i][j] = 0

while True:
    dist_map = [[0] * n for _ in range(n)]  # 거리 정보는 매번 초기화 해줘야 함
    x, y, dist = bfs(x, y, dist_map, shark_map)
    if dist == -1:
        break
    else:
        answer += dist

print(answer)

# 문제 푸는데 헤멨던 부분
# 1. 정렬
# 2. 문제 제대로 안 읽어서 상어 몸무게 키우는 로직 잘못짬
#   먹은 상어 몸무게를 더했음
#   먹은 상어 수 게이지를 초기화 안해줬음,, 누적 되는 줄ㅎㅎ
# 3. 상어 몸무게랑 같은 경우에는 큐에 추가를 안했었음. ㅋㅋ 앞으로 가려면 어찌됐든 추가해야하는데!!