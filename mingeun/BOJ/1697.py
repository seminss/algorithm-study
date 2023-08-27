n, k = map(int, input().split(' '))
# bfs
from collections import deque
# (위치, 걸린 시간)
q = deque([(n, 0)])
visited = [False] * 100001
visited[n] = True
while q:
    p, t = q.popleft()
    if p == k:
        print(t)
        break
    for pn in [p-1, p+1, 2*p]:
        err = pn
        if 0 <= pn < 100001 and not visited[pn]:
            visited[pn] = True
            q.append((pn, t+1))
