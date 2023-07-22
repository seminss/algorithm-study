'''2023.7.20
-1
'''
def solution(board):
    if len(board) == 1:
        return max(board[0])
    answer = 0
    n, m= len(board), len(board[0])
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
                answer = max(answer, board[i][j])
            
    return answer * answer
