# 2x2 블록을 지우고 지운 블록 개수를 반환
def erase(m, n, board):
    dx = [0, 1, 1]
    dy = [1, 0, 1]
    count = 0

    targets = []
    for x in range(m - 1):
        for y in range(n - 1):
            if board[x][y] == '0':
                continue
            block = board[x][y]
            for i in range(3):
                nx, ny = x + dx[i], y + dy[i]
                if board[nx][ny] != block:
                    break
            else:
                targets.append((x, y))

    for target in targets:
        x, y = target
        if board[x][y] != '0':
            count += 1
            board[x] = board[x][:y] + '0' + board[x][y + 1:]
        for i in range(3):
            nx, ny = x + dx[i], y + dy[i]
            if board[nx][ny] != '0':
                count += 1
                board[nx] = board[nx][:ny] + '0' + board[nx][ny + 1:]

    return count


# 블록을 내린 board를 반환하는 함수
def down(m, n, board):
    # 시계방향으로 돌리고
    result = list(map(list, zip(*board[::-1])))

    # 블록을 내린다
    for i in range(len(result)):
        line = ''.join(result[i])
        line = line.replace('0', '')
        line += '0' * (m - len(line))
        result[i] = line

    # 다시 반시계로 돌린다.
    result = list(map(list, zip(*result)))[::-1]
    result = [''.join(r) for r in result]
    print(result)

    return result


def pb(bo):
    for i in bo:
        print(i)
    print()


def solution(m, n, board):
    answer = 0

    check = -1
    while check != 0:
        check = erase(m, n, board)
        answer += check
        board = down(m, n, board)

    return answer