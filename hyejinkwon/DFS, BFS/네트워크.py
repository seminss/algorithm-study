from collections import deque

def BFS(v, visited, computers) :
    queue = deque()
    queue.append(v)
    n = len(computers)
    
    queue.append(v)
    visited[v] = True
    
    while queue :
        vv = queue.popleft()
        visited[vv] = True
        
        for i in range(n) :
            if i != vv and computers[vv][i] and not visited[i] :
                queue.append(i)

def solution(n, computers):
    answer = 0
    visited = [False]*n
    
    for i in range(n) :
        if not visited[i] :
            BFS(i,visited, computers)
            answer += 1
            
    return answer