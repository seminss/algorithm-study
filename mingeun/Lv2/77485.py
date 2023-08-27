'''2023.7.14
22:49 ~ 23:23
'''
X, Y = 0, 1
    
def route(p1, p2):
    """
    직사각형 테두리들의 좌표를 리스트 형태로 반환
    """
    w, h = p2[Y] - p1[Y], p2[X] - p1[X]
    direction = 0
    p = [p1[X], p1[Y]]
    results = []
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    while direction < 4:
        # 가로 방향 이동
        if direction == 0 or direction == 2: cnt = w
        # 세로 방향 이동
        elif direction == 1 or direction == 3: cnt = h
        for _ in range(cnt):
            p[X], p[Y] = p[X] + dx[direction], p[Y] + dy[direction]
            results.append(list(p))
        direction += 1
    return results
             
                
def solution(rows, columns, queries):
    # 초기화
    value = 1
    board = [[0]*columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            board[i][j] = value
            value += 1
            
    r, c = rows-1, columns-1
    answer = []
    for q in queries:
        p1 = [q[0]-1, q[1]-1]
        p2 = [q[2]-1, q[3]-1]
        points = route(p1, p2)
        v = board[p1[X]][p1[Y]]
        m = v
        # 회전
        for p in points:
            m = min(m, v)
            tmp = board[p[X]][p[Y]]
            board[p[X]][p[Y]] = v
            v = tmp
        answer.append(m)
    return answer
