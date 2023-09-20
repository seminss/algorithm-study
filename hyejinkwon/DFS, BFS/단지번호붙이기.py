import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
graph = []
answer = []

for _ in range(N) :
    graph.append(list(map(int, input().rstrip())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def BFS(x,y, graph) :
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    count  = 1

    while queue :
        x,y = queue.popleft()

        for i in range(4) :
            xx = x + dx[i]
            yy = y + dy[i]

            if xx < 0 or xx >= N or yy < 0 or yy >= N :
                continue
            
            print(xx,yy, end='  ')
            if graph[xx][yy] == 1 :
                graph[xx][yy] = 0 # visited 체크
                queue.append((xx,yy))
                count += 1
    return count

for i in range(N) :
    for j in range(N) :
        if graph[i][j] == 1 :
            answer.append(BFS(i,j,graph))

answer.sort()
print(len(answer))
for a in answer: print(a)