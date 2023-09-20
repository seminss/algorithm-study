import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
graph = []

for _ in range(N) :
    graph.append(list(map(int,input().rstrip())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def BFS(x,y, graph) :
    queue = deque()
    queue.append((x,y))

    while queue :
        x,y = queue.popleft()

        for i in range(4) :
            xx = x + dx[i]
            yy = y + dy[i]

            if 0<=xx<N and 0<=yy<M and graph[xx][yy] == 1 :
                queue.append((xx,yy))
                graph[xx][yy] = graph[x][y] + 1

BFS(0,0,graph) 
print(graph[N-1][M-1])