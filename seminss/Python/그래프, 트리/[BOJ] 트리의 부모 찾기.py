import sys
sys.setrecursionlimit(10**9)

def dfs(graph,v,answer):
    for i in graph[v]:
        if answer[i]==0:
            answer[i]=v
            dfs(graph,i,answer)

n=int(sys.stdin.readline())
answer=[0]*(n+1)
graph=[[] for _ in range(n+1)]

for i in range(n-1):
    a,b=map(int,sys.stdin.readline().split())
    graph[b].append(a)
    graph[a].append(b)

dfs(graph,1,answer)
for i in range(2,len(answer)): print(answer[i])

#메모리 초과가 났었는데, 재귀 깊이를 늘려 해결했다.