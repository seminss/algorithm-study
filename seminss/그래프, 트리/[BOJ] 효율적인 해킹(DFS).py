# 메모리 초과,, 이 문제는 파이썬은 DFS로 풀 수
import sys
sys.setrecursionlimit(10**7)

def dfs(visited,answer,graph,start):
    for i in graph[start]:
        if visited[start]==False:
            dfs(visited,answer,graph,i)
            answer[start]+=1+answer[i]
        else:
            continue
    visited[start]=True

n,m=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[b].append(a)
answer=[0]*(n+1)
visited=[False]*(n+1)

for j in range(1,n+1):
    if not visited[j]:
        dfs(visited,answer,graph,j)

mx=max(answer)
for idx,w in enumerate(answer):
    if w==mx:
        print(idx,end=" ")