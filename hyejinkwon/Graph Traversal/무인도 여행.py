# 상하좌우 연결되는 땅 -> 하나의 무인도
# 상하좌우 합 : 최대 며칠동안 머무를 수 있는지 
# 오름차순 출력

from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def BFS(visited, maps, x,y) : 
        queue = deque()
        queue.append((x,y))
        visited[x][y] = True
        value = int(maps[x][y])
        
        while queue :
            pop_x, pop_y = queue.popleft()
            for k in range(4) :
                xx = dx[k] + pop_x
                yy = dy[k] + pop_y

                if 0<= xx <len(maps) and 0<= yy <len(maps[0]) and visited[xx][yy] == False and maps[xx][yy] != "X" :
                    value += int(maps[xx][yy])
                    visited[xx][yy] = True
                    queue.append((xx,yy))
        
        return value
    
def DFS(visited, maps, x,y) : 
    visited[x][y] = True
    value = int(maps[x][y])
    
    for k in range(4) :
        xx = dx[k] + x
        yy = dy[k] + y

        if 0<= xx <len(maps) and 0<= yy <len(maps[0]) and visited[xx][yy] == False and maps[xx][yy] != "X" :
            value += DFS(visited, maps, xx, yy)
        
    return value

def solution(maps):
    answer = []
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
                    
    for i in range(len(maps)) :
        for j in range(len(maps[0])) :
            if maps[i][j] != "X" and visited[i][j] != True :
                #answer.append(BFS(visited, maps, i,j))            
                answer.append(DFS(visited, maps, i,j))   
    
    if answer == [] : 
        answer = [-1]
    else :
        answer.sort()
        
    return answer