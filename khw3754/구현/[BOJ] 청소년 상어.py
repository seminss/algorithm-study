import sys
from collections import deque

def printB(board):
    for b in board:
        print(*b)
    print()

def deepcopy(board):
    result = [[], [], [], []]
    for y in range(4):
        for x in range(4):
            result[y].append(board[y][x][::])

    return result


dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

board = []
for _ in range(4):
    line = []
    fishes = list(map(int, sys.stdin.readline().split()))
    for i in range(4):
        line.append([fishes[i*2], fishes[i*2 + 1]])
    board.append(line)

eat_max = board[0][0][0]
board[0][0][0] = -1

# 물고기들을 이동시키는 함수
def moveFish(board):
    for target in range(1, 17):
        next = False
        for y in range(4):
            if next:
                break
            for x in range(4):
                targetNum = board[y][x][0]
                targetDir = board[y][x][1]
                if targetNum == target:
                    # 이동
                    # 가능한 방향을 찾음
                    for i in range(9):
                        if i != 0:
                            targetDir += 1
                        if targetDir > 8:
                            targetDir = 1
                        nx, ny = x + dx[targetDir], y + dy[targetDir]
                        if 0 <= nx < 4 and 0 <= ny < 4 and board[ny][nx][0] != -1:
                            break
                    # 가능한 방향이 없으면 다음
                    else:
                        next = True
                        break

                    # 가능한 방향으로 물고기를 이동
                    if not next:
                        board[y][x][1] = targetDir
                        board[y][x], board[ny][nx] = board[ny][nx], board[y][x]
                    next = True
                    break

        # printB(board)

# 상어가 먹을 수 있는 물고기의 좌표의 리스트를 반환하는 함수
def canEat(board):
    result = []
    sharkPos = [-1, -1]
    sharkDir = 0
    for y in range(4):
        for x in range(4):
            if board[y][x][0] == -1:
                sharkPos = [x, y]
                sharkDir = board[y][x][1]
                break

    for i in range(1, 4):
        nx, ny = sharkPos[0] + dx[sharkDir] * i, sharkPos[1] + dy[sharkDir] * i
        if 0 <= nx < 4 and 0 <= ny < 4 and board[ny][nx][0] != 0:
            result.append((nx, ny))

    return result, sharkPos


# 물고기 이동을 마친 상태의 보드가 들어가는 큐 (보드, 먹은 물고기 번호 합)
q = deque()
moveFish(board)
q.append((board, eat_max))

while q:
    tmpBoard, tmpEatSum = q.popleft()
    canList, sharkPos = canEat(tmpBoard)

    for cx, cy in canList:
        # 먹을 수 있는 물고기를 먹음
        if eat_max < tmpEatSum + tmpBoard[cy][cx][0]:
            eat_max = tmpEatSum + tmpBoard[cy][cx][0]
        copyBoard = deepcopy(tmpBoard)
        copyBoard[cy][cx][0] = -1
        copyBoard[sharkPos[1]][sharkPos[0]] = [0, 0]

        # 물고기 이동
        moveFish(copyBoard)
        q.append((copyBoard, tmpEatSum + tmpBoard[cy][cx][0]))


print(eat_max)