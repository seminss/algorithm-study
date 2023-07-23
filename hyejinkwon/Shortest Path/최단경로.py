import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

V,E = map(int,input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
visited = [False] *(V+1)
distance = [INF] * (V+1)


for _ in range(E) :
    u,v,w = map(int,input().split())
    graph[u].append((w,v))
    
def dijkstra(start) : 
    queue = []
    heapq.heappush(queue, (0,start))
    distance[start] = 0
    
    while queue :
        d,v = heapq.heappop(queue)
        
        if distance[v] < d :
            continue
        
        for dd, vv in graph[v] :
            cost = d + dd
            
            if cost < distance[vv] :
                distance[vv] = cost
                heapq.heappush(queue, (cost,vv))
            
dijkstra(K)
for d in range(1, V+1) :
    if distance[d] == INF : 
        print("INF")
    else :
        print(distance[d])
    