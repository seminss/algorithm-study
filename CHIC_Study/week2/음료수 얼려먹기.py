#connected component 찾는 문제로도 볼 수 있다.

#DFS로 특정 노드 방문하고 연결된 모든 노드들 방문
def dfs(x,y):
    #주어진 범위를 벗어나는 경우에는 즉시 종료
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    
    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

n,m=map(int,input().split())

#2차원 리스트의 맵 정보 입력받기
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

#모든 노드(위치)에 대하여 음료수 채우기
result=0
for i in range(n):
    for j in range(m):
        #현재 위치에서 DFS 수행, 해당 노드가 방문처리 되어있으면 result+1
        if dfs(i,j)==True:
            result+=1
print(result)