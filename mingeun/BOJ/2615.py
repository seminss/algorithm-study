'''
2023.8.25
-1
'''

import sys
from collections import deque

input = sys.stdin.readline
BLACK, WHITE, EMPTY = 1, 2, 0


def bfs(checker_board, i, j, visited, direction):
    """
    checker_board[i][j] 는 EMPTY가 아니다.
    """
    BOARD_SIZE = len(checker_board)
    color = checker_board[i][j]
    # 하 우하 우 우상
    dx, dy = [1, 1, 0, -1], [0, 1, 1, 1]
    reverse_coefficient = [-1, 1]
    partial_length = [0, 0]
    positions = [(i, j)]
    # 🚨6개 이상 이어진 경우 인정되지 않는다.
    for k in range(2):
        q = deque([(i, j, 1)])  # (i, j, length_of_stone)
        visited[i][j] = True
        while q:
            x, y, length = q.popleft()
            partial_length[k] = length
            xn, yn = x + reverse_coefficient[k] * dx[direction], \
                    y + reverse_coefficient[k] * dy[direction]
            if 0 <= xn < BOARD_SIZE and 0 <= yn < BOARD_SIZE \
                    and checker_board[xn][yn] == color and not visited[xn][yn]:
                visited[xn][yn] = True
                q.append((xn, yn, length + 1))
                positions.append((xn, yn))
    # 🚨방향에 따라 시작 좌표를 다르게 출력한다.
    # 세로 방향
    if direction == 0:
        return (sum(partial_length) - 1, sorted(positions, key=lambda p: p[0])[0])
    # 대각선, 가로 방향
    else:
        return (sum(partial_length) - 1, sorted(positions, key=lambda p: p[1])[0])


def linked_length_and_position(checker_board, i, j):
    if checker_board[i][j] == EMPTY:
        return (EMPTY, (i, j))
    else:
        BOARD_SIZE = len(checker_board)
        length = 0
        for direction in range(4):
            visited = [[False] * BOARD_SIZE for _ in range(BOARD_SIZE)]
            length, position = bfs(checker_board, i, j, visited, direction)
            if length == 5:
                return (length, position)
        return (length, (0, 0))


def figure_winner(checker_board):
    DRAW = 0
    BOARD_SIZE = len(checker_board)
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            length, position = linked_length_and_position(checker_board, i, j)
            if length == 5:
                return (checker_board[i][j], position)
    return (DRAW, (0, 0))


def solution():
    BOARD_SIZE = 19
    checker_board = [list(map(int, input().split(' '))) for _ in range(BOARD_SIZE)]

    answer = figure_winner(checker_board)

    if answer[0] == 0:
        print(answer[0])
    else:
        print(answer[0])
        print(answer[1][0] + 1, answer[1][1] + 1)


solution()
