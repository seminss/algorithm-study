#2:20~3:02
import sys
from collections import deque
# R, C, N (R개의 행, C개의 열, N초가 지난 상태 출력)
R,C,N=map(int,sys.stdin.readline().split())

maps=[list(sys.stdin.readline().strip()) for _ in range(R)]
bomb=[]
dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(bomb,maps):
    dq=deque(bomb)
    new_maps=[['O']*C for _ in range(R)]
    while dq:
        x,y=dq.popleft()
        new_maps[y][x]='.'
        maps[y][x]='.'
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if ny<0 or nx<0 or ny>=R or nx>=C:
                continue
            maps[ny][nx]='.'
            new_maps[ny][nx]='.'
    return new_maps

#N이 홀수면 그냥 R,C가 다 0인 상태
if N%2==0:
    maps=[['O']*C for _ in range(R)]
else:
    for w in range((N-1)//2):
        bomb.clear()
        for i in range(R):
            for j in range(C):
                if maps[i][j]=='O':
                    bomb.append((j,i))
        maps=bfs(bomb,maps)

for i in range(R):
    print("".join(maps[i]))
