import sys
from collections import deque


M, N = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
visited = [[False for _ in range(M)] for _ in range(N)]

q = deque()
# 현재 1의 좌표를 넣어줌
for y in range(N):
    for x in range(M):
        if board[y][x] == 1:
            q.append((x, y))
            visited[y][x] = True

# 0을 모두 1로 바꿔줌
for y in range(N):
    for x in range(M):
        if board[y][x] == 0:
            board[y][x] = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# 1을 전염
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and board[ny][nx] == 1:
            board[ny][nx] += board[y][x]
            q.append((nx, ny))
            visited[ny][nx] = True

def result(board, visited):
    # 가장 큰 수를 구함
    maxi = 1
    for y in range(N):
        for x in range(M):
            if board[y][x] == 1 and not visited[y][x]:
                print(-1)
                return
            if board[y][x] > maxi:
                maxi = board[y][x]

    print(maxi-1)

result(board, visited)