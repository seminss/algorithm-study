'''2023.7.15
-1
'''
EMPTY, NEMMO = 0, 1
X, Y = 0, 1

cnt = 0

def dfs(board, k):
    global cnt
    n, m = len(board)-1, len(board[0])-1
    if k == n*m:
        cnt += 1
        return
    else:
        x, y = k // m + 1, k % m + 1
        # 넴모를 놓는 경우
        if board[x-1][y-1] == EMPTY or board[x][y-1] == EMPTY or board[x-1][y] == EMPTY:
            board[x][y] = NEMMO
            dfs(board, k+1)
            board[x][y] = EMPTY
        # 넴모를 두지 않는 경우
        dfs(board, k+1)


def solution():
    n, m = map(int, input().split(' '))
    board = [[EMPTY]*(m+1) for _ in range(n+1)]
    dfs(board, 0)
    print(cnt)

solution()
