import sys

def dfs(u,visited):
    visited.add(u)
    checked[u]=True
    for v in g[u]:
        if v not in visited:
            dfs(v, visited.copy())
        else: #사이클이 생기면 뽑는다(?)
            result.extend(list(visited))
            return

n=int(sys.stdin.readline().strip())
g=[list() for _ in range(n+1)]
for i in range(1,n+1):
    v=int(sys.stdin.readline().strip())
    g[v].append(i)

checked=[False for _ in range(n+1)]
result=[]
for i in range(1, n+1):
    if not checked[i]:
        dfs(i,set([]))

result.sort()
print(len(result))
for n in result:
    print(n)