def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v]=True
    print(v,end='')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

graph=[
    [], #그래프는 1번부텉 시작하는 경우가 많기 때문에 0번 노드는 비워둠
    [2,3,8],
    [1,7],
    [1,4,5]
]

#각 노드가 방문된 정보를 표현(1차원 리스트)
visited=[False]*4

#정의된 DFS 함수 호출
dfs(graph,1,visited)