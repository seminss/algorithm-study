import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N = int(input())
graph = [[]*(N+1) for _ in range(N+1)]
visited = [False] *(N+1)
parent = {}

for _ in range(N-1) :
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

'''
def DFS(start) :
    visited[start] = True
    
    for i in graph[start] :
        if not visited[i] :
            parent[i] = start
            DFS(i)

DFS(1)
'''

def BFS(start) :
    queue = deque([start])
    visited[start] = True

    while queue :
        pop_q = queue.popleft()

        for i in graph[pop_q] :
            if not visited[i] :
                queue.append(i)
                parent[i] = pop_q
                visited[i] = True

BFS(1)

for i in range(2,N+1) :
    if i in parent :
        print(parent[i])

