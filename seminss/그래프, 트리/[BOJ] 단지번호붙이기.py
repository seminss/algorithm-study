import sys
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y,visited):
    queue=[(x,y)]
    visited[y][x]=0
    result=1
    while queue:
        x,y=queue.pop(0)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=len(visited) or ny<0 or ny>=len(visited):
                continue
            if visited[ny][nx]==1:
                result+=1
                queue.append((nx,ny))
                visited[ny][nx]=0
    return result


n=int(sys.stdin.readline())
sq=list(list(map(int,sys.stdin.readline().strip())) for _ in range(n))
visited=sq.copy()
total_cnt=0 #전체 단지 몇개?
each_cnt=[]

for i in range(len(sq)):
    for j in range(len(sq[i])):
        if visited[i][j]==1:
            each_cnt.append(bfs(j,i,visited))
            total_cnt+=1

each_cnt.sort()
print(total_cnt)
for e in each_cnt:
    print(e)