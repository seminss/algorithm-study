import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [] 
for _ in range(N) :
    graph.append(list(map(int,input().split())))

# 플로이드 워셜
for i in range(N) :
     for j in range(N) : 
         for k in range(N) :
            if graph[j][i] and graph[i][k] : 
                graph[j][k] = 1

for g in graph :
    print(*g)     