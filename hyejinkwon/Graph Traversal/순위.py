from collections import deque

def solution(n, results):
    answer = 0
    queue = deque()
    graph = [[0]*n for _ in range(n)]
    
    for x,y in results :
        graph[x-1][y-1] = 1
        graph[y-1][x-1] = -1
        
    '''
    a->b 이기고 b->c 이기면 a->c 이긴것.
    b->a c->b c->a 는 모두 졌다.
    '''
    
    for k in range(n) :
        for i in range(n) :
            for j in range(n) :
                if graph[i][k] == graph[k][j] == 1:
                    graph[i][j] = 1
                    graph[j][i] = graph[k][i] = graph[j][k] = -1
        
    for g in graph :
        if g.count(0) == 1:
            answer += 1
    
    return answer