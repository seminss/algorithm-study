import sys
from collections import deque

input = sys.stdin.readline
N ,M = map(int, input().split())

graph = [[] for _ in range(N+1)]
answer_list = []

for m in range(M) :
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def BFS(graph, start, visited) :
    answer = [0] * (N+1)
    queue = deque([start])
    visited[start] = True

    while queue :
        v = queue.popleft()
        
        for i in graph[v] :
            if not visited[i] :
                answer[i] = answer[v] + 1
                visited[i] = True
                queue.append(i)
    
    return sum(answer)

for i in range(1,N+1) :
    visited = [False] * (N+1)
    answer_list.append(BFS(graph,i,visited))

print(answer_list.index(min(answer_list))+1 )


    