import sys
from collections import deque

def DFS(graph,v,visited):
    visited[v]=True
    print(v,end=' ')
    graph[v].sort() #방문 가능한 정점이 여러개면, 정점 번호가 작은 것부터
    for i in graph[v]:
        if not visited[i]:
            DFS(graph,i,visited)

def BFS(graph,start,visited):
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        print(v,end=' ')
        graph[v].sort()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

n,m,v=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]

#0은 비워둔다. 인덱스가 1부터 시작하니까
for i in range(m):
    x,y=map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

dfs_visited=[False]*(n+1) #노드 방문 정보
bfs_visited=[False]*(n+1)

DFS(graph,v,dfs_visited)
print()
BFS(graph,v,bfs_visited)
