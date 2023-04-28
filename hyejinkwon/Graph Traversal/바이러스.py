import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
pair = int(input())
graph = [[]*(N+1) for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(pair) :
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0 

# def DFS(graph, start, visited) :
#     global count
#     visited[start] = True
#     count += 1

#     for i in graph[start] :
#         if not visited[i] :
#             DFS(graph,i,visited)

# DFS(graph,1,visited)
# print(count-1)

def BFS(graph,start,visited) :
    global count

    queue = deque([start])
    visited[start] = True

    while queue :
        pop_queue = queue.popleft()
        count += 1

        for i in graph[pop_queue] : 
            if not visited[i] :
                queue.append(i)
                visited[i] = True

    return count

print(BFS(graph,1,visited)-1)

