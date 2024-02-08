R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]


def spray(board):
    # [[r, c, 확산된 양], ...]
    targets = []
    for r in range(R):
        for c in range(C):
            if board[r][c] > 4:
                aroundBlocks = getAroundBlocks(board, r, c)
                targets.extend(aroundBlocks)
                board[r][c] -= (board[r][c] // 5) * len(aroundBlocks)

    for r, c, amount in targets:
        board[r][c] += amount


def getAroundBlocks(board, r, c):
    result = []
    amount = board[r][c] // 5
    R_checkList = [r - 1, r + 1]
    C_checkList = [c - 1, c + 1]

    for CL in R_checkList:
        if 0 <= CL < R and board[CL][c] != -1:
            result.append([CL, c, amount])
    for CL in C_checkList:
        if 0 <= CL < C and board[r][CL] != -1:
            result.append([r, CL, amount])
    return result

def cycleAir(board):
    for i in range(R):
        if board[i][0] == -1:
            upRC = [i, 0]
            downRC = [i + 1, 0]
            break

    coor = (upRC[0], 1)
    lastAmount = 0
    while True:
        if board[coor[0]][coor[1]] == -1:
            break

        next = nextblock(coor[0], coor[1], 'up')
        lastAmount, board[coor[0]][coor[1]] = board[coor[0]][coor[1]], lastAmount
        coor = next


    coor = (downRC[0], 1)
    lastAmount = 0
    while True:
        if board[coor[0]][coor[1]] == -1:
            break

        next = nextblock(coor[0], coor[1], 'down')
        lastAmount, board[coor[0]][coor[1]] = board[coor[0]][coor[1]], lastAmount
        coor = next

def nextblock(r, c, upOrDown):
    if 0 < r < R - 1 and 0 < c < C - 1:
        return (r, c + 1)

    if 0 < r < R - 1 and c == C - 1:
        if upOrDown == 'up':
            return (r - 1, c)
        if upOrDown == 'down':
            return (r + 1, c)

    if (r == 0 or r == R - 1) and 0 < c < C:
        return (r, c - 1)

    if upOrDown == 'up':
        return (r + 1, c)
    elif upOrDown == 'down':
        return (r - 1, c)



for _ in range(T):
    spray(board)
    cycleAir(board)

result = 2
for row in board:
    result += sum(row)

print(result)