# 9:40~
import sys
from collections import deque

dx=[-1,1,0,0,1,-1,1,-1]
dy=[0,0,-1,1,1,-1,-1,1]

def bfs(x,y,maps,visited):
    que=deque([(x,y)])
    visited[y][x]=True
    while que:
        x,y=que.popleft()
        for _ in range(8):
            nx=x+dx[_]
            ny=y+dy[_]
            if nx<0 or ny<0 or nx>=w or ny>=h:
                continue
            if maps[ny][nx]==1 and not visited[ny][nx]:
                visited[ny][nx]=True
                que.append((nx,ny))



w,h=map(int,sys.stdin.readline().split())

while (w,h)!=(0,0):
    maps = [[] for _ in range(h)]
    for i in range(h):
        maps[i]=list(map(int,sys.stdin.readline().split()))
    visited=[[False]*w for _ in range(h)]
    island=0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and maps[i][j]==1:
                bfs(j,i,maps,visited)
                island+=1
    print(island)
    w,h=map(int,sys.stdin.readline().split())
