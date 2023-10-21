from collections import deque

def solution(n, edge):
    answer = 0
    queue = deque()
    graph = [[] for _ in range(n)]
    distance = [-1]*n

    for x,y in edge :
        graph[x-1].append(y-1)
        graph[y-1].append(x-1)
        
    queue.append(0)
    distance[0] = 1
    
    while queue :
        q = queue.popleft()
        
        for v in graph[q] :
            if distance[v] == -1 :
                queue.append(v)
                distance[v] = distance[q] + 1
    
    max_distance = max(distance)
    for d in distance :
        if max_distance == d : answer += 1
    
    return answer