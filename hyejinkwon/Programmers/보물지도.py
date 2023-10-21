from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def solution(n, m, hole):
    answer = 0
    
    map = [[1]*m for _ in range(n)]
    # x,y, 신발사용여부
    visited = [ [[False]*2 for _ in range(m)] for _ in range(n)]

    for x,y in hole :
        map[x-1][y-1] = 0
        
    de = deque()
    de.append((0,0,False))
    visited[0][0][False] = True
    val = 0
    
    while de :
        for _ in range(len(de)) : 
            vx, vy, shoes = de.popleft()

            for k in range(4) :
                xx = vx + dx[k]
                yy = vy + dy[k]

                if 0<=xx<n and 0<=yy<m and not visited[xx][yy][shoes] and map[xx][yy] == 1 :
                    if xx == n-1 and yy == m-1 : return val+1

                    visited[xx][yy][shoes] = True
                    de.append([xx,yy,shoes])

                if not shoes :
                    xx += dx[k]
                    yy += dy[k]
                    if 0<=xx<n and 0<=yy<m and not visited[xx][yy][True] and map[xx][yy] == 1 :
                        if xx == n-1 and yy == m-1 : return val+1

                        visited[xx][yy][True] = True
                        de.append([xx,yy,True])
        val += 1
    
    return -1