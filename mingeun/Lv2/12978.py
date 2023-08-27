'''2023.7.18
17:52 ~ 18:23
'''

from collections import deque
def solution(N, road, K):
    INF = 99999999
    answer = 0
    data = [ [INF] * (N+1) for _ in range(N+1) ]
    for u, v, w in road:
        data[u][v] = min(data[u][v], w)
        data[v][u] = min(data[v][u], w)
    for i in range(1, N+1):
        data[i][i] = 0
    # Floyd-Warshall's
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                data[i][j] = min(data[i][k] + data[k][j], data[i][j])
                
    for r in data:
        print(r)
        
    answer = 0
    for i in range(1, N + 1):
        if data[1][i] <= K:
            answer += 1
    return answer
