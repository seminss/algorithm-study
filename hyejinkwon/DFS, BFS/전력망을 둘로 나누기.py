from collections import deque

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n)]
    
    for i,j in wires :
        graph[i-1].append(j-1)
        graph[j-1].append(i-1)
        
    def BFS(v) :
        visited = [False]*n
        
        queue = deque()
        queue.append(v)
        visited[v] = True
        count = 1
        
        while queue : 
            vv = queue.popleft()
            for i in graph[vv] :
                if not visited[i] :
                    visited[i] = True
                    queue.append(i)
                    count += 1
        return count
    
    for i,j in wires :
        graph[i-1].remove(j-1)
        graph[j-1].remove(i-1)
        
        answer = min(answer, abs(BFS(i-1) - BFS(j-1)))
        
        graph[i-1].append(j-1)
        graph[j-1].append(i-1)
    
    
    return answer