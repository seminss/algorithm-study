'''2023.6.16
12:14 ~ 12:36
'''
def solution(n):
    """
    01
    02 12
    03 13 11
    04 14 15 10
    05 06 07 08 09
    
    d[0] 방향: l(5) 만큼 이동 ([0][0], [1][0], [2][0], [3][0], [4][0]), l-=1
    d[1] 방향: l(4) 만큼 이동 ([4][1], [4][2], [4][3], [4][4]), l-=1
    d[2] 방향: l(3) 만큼 이동 ([3][3], [2][2], [1][1]), l-=1
    """
    data = [[0]*i for i in range(1, n+1)]
    didx = 0 # 방향 결정
    d = [(1, 0), (0, 1), (-1, -1)] # 이동 방향
    X, Y = 0, 1
    l = n # 이동해야 하는 거리
    value = 0
    x, y = -1, 0
    
    while value < n*(n+1)//2:
        # d[didx] 방향으로 l만큼 이동
        for _ in range(l):
            value += 1
            x, y = x + d[didx][X], y + d[didx][Y]
            data[x][y] = value
            # print(f'data[{x}][{y}] = {value}')
        # l만큼 이동 후 방향 전환, l 감소
        didx = (didx+1)%3
        l -= 1
    answer = []
    for d in data:
        answer += d
    return answer

