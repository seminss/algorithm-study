#dfs
import sys

def dfs(x,y,visited):
    if graph[x][y]=='-' and visited[x][y]==False:
        visited[x][y]=True
        if (y+1>0 and y+1<m) and graph[x][y+1]=='-':
            dfs(x,y+1,visited)
        #x,y가 오름차순으로 가기 때문에 + 방향만 봐주면 된다.
    if graph[x][y]=='|' and visited[x][y]==False:
        visited[x][y]=True
        if (x+1>0 and x+1<n) and graph[x+1][y]=='|':
            dfs(x+1,y,visited)

n,m =map(int,sys.stdin.readline().split())

#2차원 리스트의 맵 정보 입력
graph=[]
for i in range(n):
    graph.append(sys.stdin.readline().strip())
visited=[[False]*m for _ in range(n)]
result=0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i,j,visited)
            result+=1
print(result)