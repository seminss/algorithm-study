import sys
from collections import deque

input = sys.stdin.readline

M,N,H = map(int, input().split())
box  = [] 
queue = deque([])

for _ in range(H) :
    row = []
    for _ in range(N) :
        row.append(list(map(int,input().split())))
    box.append(row)

for i in range(H) :
    for j in range(N) :
        for l in range(M) :
            if box[i][j][l] == 1 :
                queue.append([i,j,l])

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

if len(queue) == N*M*H :
    print(0)
    exit(0)

def BFS() :
    while queue :
        x,y,z = queue.popleft()
        for k in range(6) :
            xx = x+dx[k]
            yy = y+dy[k]
            zz = z+dz[k]

            if 0<=xx<H and 0<=yy<N and 0<=zz<M and box[xx][yy][zz] == 0:
                box[xx][yy][zz] = box[x][y][z] + 1
                queue.append([xx,yy,zz])

BFS()

day = 0

for i in box :
    for j in i :
        if 0 in j :
            print(-1)
            exit(0)
        day = max(day, max(j))

print(day-1)

         