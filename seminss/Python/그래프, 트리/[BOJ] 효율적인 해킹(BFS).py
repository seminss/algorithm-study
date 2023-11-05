import sys
from collections import deque


def bfs(visited, answer, graph, start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
    answer[start] = visited.count(True)


n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)

answer = [0] * (n + 1)
stack = []

for j in range(1, n + 1):
    visited = [False] * (n + 1)
    bfs(visited, answer, graph, j)

mx = max(answer)
for idx, w in enumerate(answer):
    if w == mx:
        print(idx, end=" ")
