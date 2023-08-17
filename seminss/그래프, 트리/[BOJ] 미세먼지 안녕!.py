import sys

R, C, T = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
temp_maps = [[0] * C for _ in range(R)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

purifier = []


def one_point_spread(x, y):
    global maps
    global temp_maps
    p = maps[y][x] // 5
    for _ in range(4):
        nx = x + dx[_]
        ny = y + dy[_]
        if nx < 0 or ny < 0 or nx >= C or ny >= R:
            continue
        if maps[ny][nx] == -1:
            continue
        temp_maps[ny][nx] += p
        temp_maps[y][x] -= p


def up_cycle(purifier):
    global maps
    px, py = purifier
    x, y = px, py - 1  # 공기 청정기 한 칸 위에 시작
    while y > 0:
        maps[y][x] = maps[y - 1][x]
        y -= 1
    while x < C - 1:
        maps[y][x] = maps[y][x + 1]
        x += 1
    while y < py:
        maps[y][x] = maps[y + 1][x]
        y += 1
    while x > 0:
        maps[y][x] = maps[y][x - 1]
        x -= 1
    maps[py][px + 1] = 0


def bottom_cycle(purifier):
    global maps
    px, py = purifier
    x, y = px, py + 1  # 공기 청정기 한 칸 아래서 시작
    while y < R - 1:
        maps[y][x] = maps[y + 1][x]
        y += 1
    while x < C - 1:
        maps[y][x] = maps[y][x + 1]
        x += 1
    while y > py:
        maps[y][x] = maps[y - 1][x]
        y -= 1
    while x > 0:
        maps[y][x] = maps[y][x - 1]
        x -= 1
    maps[py][px + 1] = 0


for cnt in range(T):
    for i in range(R):
        for j in range(C):
            if maps[i][j] == -1:
                purifier.append((j, i))
            if maps[i][j] > 0:  # 확산 되는거 파악
                one_point_spread(j, i)
    for i in range(R):  # maps 갱신
        for j in range(C):
            maps[i][j] += temp_maps[i][j]
            temp_maps[i][j] = 0

    up_cycle(purifier[0])
    bottom_cycle(purifier[1])
    purifier.clear()

total_dust = 0
for row in maps:
    total_dust += sum(row)
print(total_dust + 2)

# 로직은 간단했는데 방향이 너무 헷갈렸다!! ㅜ.ㅜ
