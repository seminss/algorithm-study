''' 2023.5.10
16:53 ~ 16:58
'''
def solution(x, y, n):
    # x -> y
    from collections import deque
    q = deque([(x, 0)])
    visited = [False] * 1000001
    visited[x] = True
    while q:
        p, cnt = q.popleft()
        if p == y:
            return cnt
        for pn in [p + n, p*2, p*3]:
            if 0<=pn<1000001 and not visited[pn]:
                visited[pn] = True
                q.append((pn, cnt + 1))
    return  -1
