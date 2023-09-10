''' 2023.6.2
'''
EMPTY = ' '

def erase(m, n, blocks):
    targets = set()
    dx, dy = [0, 1, 1], [1, 1, 0]
    visited = [[False] * n for _ in range(m)]
    for i in range(m-1):
        for j in range(n-1):
            # 정사각형 구역 확인
            if blocks[i][j] != EMPTY:
                character = blocks[i][j]
                cnt = 1
                tmp = [(i, j)]
                for k in range(3):
                    xn, yn = i + dx[k], j + dy[k]
                    if blocks[xn][yn] != character:
                        break
                    else:
                        tmp.append((xn, yn))
                if len(tmp) == 4:
                    for l in range(len(tmp)):
                        targets.add((tmp[l][0], tmp[l][1]))
    # erase
    result = 0
    for (i, j) in targets:
        blocks[i][j] = EMPTY
        result += 1
    return result


def rearrange(m, n, blocks):
    """
    블록이 지워진 후 위에 있는 블록들이 아래로 떨어져 빈 공간을 채운다.
    """
    # 각 열에 대해, 행을 증가시키며 비어있지 않은 블럭을 큐에 넣는다.
    not_empty_blocks = []
    for i in range(n):
        for j in range(m):
            if blocks[j][i] != EMPTY:
                not_empty_blocks.append(blocks[j][i])
                blocks[j][i] = EMPTY
        # 큐에 있던 블럭을 밑에서부터 쌓는다.
        for j in range(len(not_empty_blocks)):
            blocks[m - j - 1][i] = not_empty_blocks.pop()
            

def solution(m, n, board):
    # 문자열 배열 -> 2차원 배열 변환
    blocks = [[EMPTY] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            blocks[i][j] = board[i][j]
    answer = 0
    # 더 이상 사라질 블록이 없을 때까지 진행
    while True:
        tmp = erase(m, n, blocks)
        if tmp == 0:
            break
        answer += tmp 
        rearrange(m, n, blocks)
    return answer
