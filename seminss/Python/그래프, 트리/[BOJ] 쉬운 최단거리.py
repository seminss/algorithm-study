#1:30~1:56
import sys
from collections import deque

#행, 열
n,m=map(int,sys.stdin.readline().split())
maps=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(maps, cango,visited):
    dq=deque(cango)
    while dq:
        x,y=dq.popleft()
        visited[y][x]=True
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=m or ny>=n:
                continue
            if maps[ny][nx]==1 and visited[ny][nx]==False:
                maps[ny][nx]=maps[y][x]+1
                dq.append((nx,ny))
                
for i in range(n):
    for j in range(m):
        if maps[i][j]==2:
            x=j
            y=i

visited=[[False]*m for _ in range(n)]
maps[y][x]=0
bfs(maps,[(x,y)],visited)

for i in range(n):
    for j in range(m):
        if visited[i][j]==False and maps[i][j]==1:
            maps[i][j]=-1 #방문하지 못하는 곳
        print(maps[i][j],end=" ")
    print()