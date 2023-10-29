from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def BFS(x,y,maps) :
    queue = deque()
    queue.append([x,y])
    val = 0
    
    while queue :
        vx, vy = queue.popleft()
        
        for k in range(4) :
            xx = vx + dx[k]
            yy = vy + dy[k]
            
            if 0 > xx or xx >= len(maps) or 0 > yy or yy >= len(maps[0]) : continue
            if maps[xx][yy] == 0 : continue
            if maps[xx][yy] == 1 :    
                maps[xx][yy] = maps[vx][vy] + 1
                queue.append([xx,yy])
        
    return maps[len(maps)-1][len(maps[0])-1]

def solution(maps):
    answer = 0    
    answer = BFS(0,0,maps)    
    
    if answer == 1 : return -1
    else : return answer 