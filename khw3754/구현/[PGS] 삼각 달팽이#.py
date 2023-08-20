def nextIndex(tri, x, y, state):
    if state == 'down':
        nx, ny = x + 1, y
        if nx < len(tri) and tri[nx][ny] == 0:
            return nx, ny, state
        else:
            return x, y + 1, 'right'

    elif state == 'right':
        nx, ny = x, y + 1
        if ny < len(tri[nx]) and tri[nx][ny] == 0:
            return nx, ny, state
        else:
            return x - 1, y - 1, 'up'

    elif state == 'up':
        nx, ny = x - 1, y - 1
        if nx >= 0 and tri[nx][ny] == 0:
            return nx, ny, state
        else:
            return x + 1, y, 'down'


def solution(n):
    answer = []

    if n == 1:
        return [1]

    tri = [[0] * i for i in range(1, n + 1)]
    x, y = 0, 0
    state = 'down'
    count = 1

    # 달팽이 채우기
    while True:
        tri[x][y] = count
        count += 1

        # 다음 인덱스, 상태 계산 -> 유효하면 계속 진행
        nx, ny, nState = nextIndex(tri, x, y, state)
        if tri[nx][ny] == 0:
            x, y = nx, ny
            state = nState
        else:
            break

    # 합침
    for tmp in tri:
        answer.extend(tmp)

    return answer