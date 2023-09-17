import sys
from collections import deque

# 1:25 ~ 2:20

n, m = map(int, sys.stdin.readline().split())
computer = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    computer[b].append(a)

answer = [0] * (n + 1)

for i in range(1, n + 1):
    dq = deque([i])  # bfs
    visited = [False] * (n + 1)
    visited[i] = True
    while dq:
        num = dq.popleft()
        for c in computer[num]:
            if not visited[c]:
                dq.append(c)
                visited[c] = True
    answer[i]=visited.count(True)

for i, c in enumerate(answer):
    if c == max(answer):
        print(i, end=" ")

# bfs에서 메모리 초과가 나는 부분은 visited check를 하지 않은 경우다.
# 갔던 부분을 계속 돈다.
# 이렇게 신경써서 짜도 시간초과가 뜬다.. Pypy를 써야한다.
