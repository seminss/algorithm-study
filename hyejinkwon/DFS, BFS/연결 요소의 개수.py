import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph =[[0]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(M) :
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def BFS(start) : 
    queue = deque()
    queue.append((start))
    visited[start] = True

    while queue :
        v = queue.popleft()
        
        for vv in graph[v] : 
            if not visited[vv] :
                queue.append((vv))
                visited[vv] = True

count = 0
for i in range(1,N+1) :
    if not visited[i] :
        BFS(i)
        count += 1

print(count)