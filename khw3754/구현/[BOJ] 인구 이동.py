from collections import deque

N, L, R = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

def move():
    visited = [[False for _ in range(N)] for _ in range(N)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    changed = False
    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                numSum, group = getGroup(visited, x, y)
                average = numSum // len(group)
                for gx, gy in group:
                    if board[gy][gx] != average:
                        board[gy][gx] = average
                        changed = True
    return changed

def getGroup(visited, x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    numSum = board[y][x]
    result = [[x, y]]
    q = deque()
    q.append([x, y])
    visited[y][x] = True

    while q:
        X, Y = q.popleft()
        for i in range(4):
            nx, ny = X + dx[i], Y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and L <= abs(board[ny][nx] - board[Y][X]) <= R:
                q.append([nx, ny])
                visited[ny][nx] = True
                result.append([nx, ny])
                numSum += board[ny][nx]
    return numSum, result

day = 0
changed = move()
while changed:
    day += 1
    changed = move()


print(day)