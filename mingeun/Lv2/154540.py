'''2023.6.22
16:04 ~ 16:43
'''
from collections import deque

VISITED = '-1'

def bfs(s:list, data:list):
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    q = deque([ (s[0], s[1]) ])
    result = int(data[s[0]][s[1]])
    data[s[0]][s[1]] = VISITED
    while q:
        (x, y) = q.popleft()
        for i in range(4):
            xn, yn = x+dx[i], y+dy[i]
            if 0<=xn<len(data) and 0<=yn<len(data[0]) and data[xn][yn] != VISITED and data[xn][yn] != 'X':
                result += int(data[xn][yn])
                q.append((xn, yn))
                data[xn][yn] = VISITED
    return result

def solution(maps):
    answer = []
    data = [['']*len(maps[0]) for _ in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            data[i][j] = maps[i][j]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if data[i][j] != VISITED and data[i][j] != 'X':
                answer.append(bfs([i, j], data))
    
    if len(answer) == 0:
        answer = [-1]
    return sorted(answer)
