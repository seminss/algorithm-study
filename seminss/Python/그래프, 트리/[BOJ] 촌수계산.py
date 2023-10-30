import sys
from collections import deque

n=int(sys.stdin.readline())
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
p1,p2=map(int,sys.stdin.readline().split())
m=int(sys.stdin.readline())

for _ in range(m):
    x,y=map(int,sys.stdin.readline().strip().split())
    graph[x].append(y)
    graph[y].append(x)

que=deque([p1])
while que:
    num=que.popleft()
    for i in graph[num]:
        if visited[i]==0:
            visited[i]=visited[num]+1
            que.append(i)

print(visited[p2] if visited[p2]>0 else -1)
