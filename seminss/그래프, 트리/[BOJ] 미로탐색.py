import sys

dx=[-1,1,0,0]
dy=[0,0,-1,1]

n,m=map(int, sys.stdin.readline().split())
miro=[list(map(int,sys.stdin.readline().strip())) for _ in range(n)]

def bfs(x,y):
    queue=[(x,y)]
    miro[y][x]=0 #방문처리
    while queue:
        x,y=queue.pop(0)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            if miro[ny][nx]==1: 
                miro[ny][nx]=miro[y][x]+1 #해당 노드를 처음 방문하는 경우 최단 거리 기록
                queue.append((nx,ny))
    return miro[n-1][m-1]+1
print(bfs(0,0))