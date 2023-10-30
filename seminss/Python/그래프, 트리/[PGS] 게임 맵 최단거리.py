from collections import deque
def solution(maps):
    n=len(maps) #세로
    m=len(maps[0]) #가로
    q=deque()
    q.append((0,0))
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n and maps[ny][nx]==1:
                q.append((nx,ny))
                maps[ny][nx]=maps[y][x]+1
    if maps[n-1][m-1]==1:
        return -1
    else:
        return maps[n-1][m-1]
    
#어짜피 한번 방문한 곳은 방문할 수가 없어서, 자동으로 최단거리가 구해진다.
#maps[ny][nx]=maps[y][x]+1 이 부분에 의해서!