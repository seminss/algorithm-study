from collections import deque

def BFS(maps, visited, start) :
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    distance = [[1] * len(maps[0]) for _ in range(len(maps))]
    
    x,y = start
    queue = deque()
    visited[x][y] = True
    queue.append([x,y])
    
    while queue :
        x,y = queue.popleft()
        
        for i in range(4) :
            xx = x + dx[i]
            yy = y + dy[i]
            
            if 0<=xx<len(maps) and 0<=yy<len(maps[0]) and maps[xx][yy] == 1 and not visited[xx][yy] :
                visited[xx][yy] = True
                queue.append([xx,yy])
                distance[xx][yy] = distance[x][y] + 1
    
    if distance[len(distance)-1][len(distance[0])-1] == 1 :
        return -1
    
    else :
        return distance[len(distance)-1][len(distance[0])-1]

def solution(maps):
    answer = 0  
    visited = [[False] *len(maps[0]) for _ in range(len(maps))]     
    answer = BFS(maps,visited,[0,0])
    
    return answer