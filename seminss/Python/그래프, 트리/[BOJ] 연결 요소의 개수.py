import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph =[[] for i in range(N+1)]


for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(n,graph, visited):
    que = deque([n])
    visited[n]=True
    while que:
        node = que.popleft()
        for i in set(graph[node]):
            if not visited[i] :
                que.append(i)
                visited[i]=True

result=0
visited=[False]*(N+1)

for i in range(1,N+1):
    if not visited[i]:
        bfs(i,graph, visited)
        result+=1
print(result)

# u,v 양방향으로 삽입을 해줘야 합니다..