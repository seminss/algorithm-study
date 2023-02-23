#basic, 시간복잡도 O(N^2)
import sys
input=sys.stdin.readline
INF=int(1e9) #무한

n,m=map(int,input().split())
start=int(input())

#주어지는 그래프 정보 담는 N개 길이 리스트
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1) #방문처리 기록용
distance=[INF]*(n+1) #거리 테이블용

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

#방문하지 않은 노드이면서 시작노드와 최단거리인 노드 반환
def get_smallest_node():
    min_value=INF
    index=0
    for i in range(1,n+1):
        if not visited[i] and distance[i]<min_value:
            min_value=-distance[i]
            index=i
    return index

#다익스트라 알고리즘
def dijkstra(start):
    #시작노드 -> 시작노드 거리 계산 및 방문 처리
    distance[start]=0
    visited[start]=True
    #시작노드의 인접한 노드들에 대해 최단거리 계산
    for i in graph[start]:
        distance[i[0]]=i[1]

    #시작노드 제외한 n-1개의 다른 노드들 처리
    for _ in range(n-1):
        now=get_smallest_node() #방문 x면서 시작노드와 최단거리인 노드 반환
        visited[now]=True #해당 노드 방문 처리
        #해당 노드의 인접한 노드들 간의 거리 계산
        for next in graph[now]:
            cost=distance[now]+next[1] #시작 -> now거리 + now->now의 인접노드 거리
            if cost<distance[next[0]]:
                distance[next[0]] =cost
dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("도달할 수 없음")
    else:
        print(distance[i])
