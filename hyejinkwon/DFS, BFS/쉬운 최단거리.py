import sys 
from collections import deque

input = sys.stdin.readline
N,M =map(int,input().split())
graph = []
visited = [[False]*M for _ in range(N)]
distance = [[-1]*M for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def BFS(x,y) :
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    distance[x][y] = 0

    while queue :
        x, y = queue.popleft()

        for k in range(4) :
            xx = x + dx[k]
            yy = y + dy[k]
        
            if 0<=xx<N and 0<=yy<M and not visited[xx][yy] :
                if graph[xx][yy] == 0 : 
                    visited[xx][yy] = True
                    distance[xx][yy] = 0
                elif graph[xx][yy] == 1 :
                    visited[xx][yy] = True 
                    distance[xx][yy] = distance[x][y] + 1
                    queue.append((xx,yy))

for i in range(N) :
    A = list(map(int, input().split()))
    graph.append(A)
    if 2 in A :
        startx = i
        starty = A.index(2)

BFS(startx,starty)

for i in range(N) :
    for j in range(M) :
        if graph[i][j] == 0 : print(0 , end=" ")
        else : print(distance[i][j], end=" ")
    print()
            
