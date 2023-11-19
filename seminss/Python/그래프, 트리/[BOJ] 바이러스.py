from collections import deque

# 3:33~3:47
result = int(input())
nodes = int(input())
computers = [list() for _ in range(result + 1)]
visited = [False for _ in range(result + 1)]

for _ in range(nodes):
    a, b = map(int, input().split())
    computers[a].append(b)
    computers[b].append(a)


def bfs(edge):
    dq = deque([edge])
    visited[edge] = True
    while dq:
        edge = dq.popleft()
        for i in computers[edge]:
            if visited[i]:
                continue
            dq.append(i)
            visited[i] = True


bfs(1)
print(visited.count(True) - 1)
