import sys
sys.setrecursionlimit(10**7)

N, M = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
data.sort()

ans = []
visited=[False]*N

def back():
    if len(ans) == M:
        print(' '.join(map(str,ans)))
        return
    prev=0
    for i in range(N):
        if visited[i] or data[i]==prev:
            continue
        visited[i]=True
        ans.append(data[i])
        prev=data[i]
        back()
        visited[i]=False
        ans.pop()

back()
