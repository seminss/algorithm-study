# 원래 풀었던 방법
# 효율성 테스트 시간초과
'''
# (x, y) 에서 최대 정사각형의 넓이를 구해주는 함수
def area(board, x, y):
    # 넓이 2, 3, ... 으로 검사
    length = 1
    while True:
        if y + length >= len(board) or x + length >= len(board[0]):
            return length ** 2
        for i in range(length + 1):
            if board[y + i][x + length] != 1:
                return length ** 2
        for i in range(length + 1):
            if board[y + length][x + i] != 1:
                return length ** 2
        length += 1


# 0과 가장 왼쪽을 기준으로 오른쪽에 있는 1의 정사각형의 넓이를 구해보면 된다고 생각
def solution(board):
    answer = 0

    lastLen = 0
    for y in range(len(board)):
        lastVal = 0
        if lastLen != 0:
            lastLen -= 1
            continue
        for x in range(len(board[0])):
            if lastVal == 0 and board[y][x] == 1:
                areaTmp = area(board, x, y)
                if answer < areaTmp:
                    answer = areaTmp
            else:
                lastVal = board[y][x]

    return answer
'''

# 새 풀이
# 정답을 보고 푼 풀이
def solution(board):
    answer = 0

    for y in range(1, len(board)):
        for x in range(1, len(board[0])):
            if board[y][x] != 0:
                board[y][x] += min(board[y - 1][x - 1], board[y][x - 1], board[y - 1][x])
                if answer < board[y][x]:
                    answer = board[y][x]

    if answer == 0:
        for y in range(len(board)):
            if board[y][0] == 1:
                answer = 1
                break
        for x in range(len(board[0])):
            if board[0][x] == 1:
                answer = 1
                break

    return answer ** 2