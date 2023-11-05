#8:43~9:00
from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(sq,x,y):
    queue=[(x,y)]
    days=int(sq[y][x])
    sq[y][x]="X"
    while queue:
        x,y=queue.pop(0)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=len(sq[0]) or ny>=len(sq):
                continue
            if sq[ny][nx]!="X":
                days+=int(sq[ny][nx])
                sq[ny][nx]="X"
                queue.append((nx,ny))
    return days

def solution(maps):
    answer = []
    sq=list(list(c for c in l) for l in maps)
    for i in range(len(sq)):
        for j in range(len(sq[i])):
            if sq[i][j]!="X":
                answer.append(bfs(sq,j,i))
    if len(answer)==0:
        return [-1]
    else:
        return sorted(answer)