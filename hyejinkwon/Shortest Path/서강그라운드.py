import sys

input = sys.stdin.readline

INF = int(1e9)
N, M, R = map(int, input().split())
area_item = list(map(int, input().split()))
field = [[INF] * N for _ in range(N)]

for _ in range(R):
    a, b, l = map(int, input().split())
    field[a-1][b-1] = min(field[a-1][b-1], l)
    field[b-1][a-1] = min(field[b-1][a-1], l)

for k in range(N):
    for a in range(N):
        for b in range(N):
            field[a][b] = min(field[a][b], field[a][k] + field[k][b])
            if a == b:
                field[a][b] = 0

max_value = 0

for i in range(N):
    temp_value = 0
    for j in range(N):
        if field[i][j] <= M:
            temp_value += area_item[j]

    max_value = max(max_value, temp_value)

print(max_value)