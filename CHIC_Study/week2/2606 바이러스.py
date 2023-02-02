import sys

computer=int(sys.stdin.readline().strip())
connect=int(sys.stdin.readline().strip())
graph=[[]*computer for _ in range(computer+1)] #모든 컴퓨터가 전부 연결된 경우 가정
for i in range(connect):
    a,b =map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a) #같은 컴퓨터에 연결된 컴퓨터들을 묶기
print(graph)

cnt=0
visited=[0]*(computer+1) #1번부터 세기 위해
def dfs(start):
    global cnt
    visited[start]=1
    for i in graph[start]:
        if visited[i]==0:
            dfs(i)
            cnt+=1

dfs(1)
print(cnt)

# 입력
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7
