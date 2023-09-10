'''2023.7.14
23:38 ~ 23:50
'''
from collections import deque

def count_tower(matrix, start, n):
    q = deque([start])
    visited = [False] * (n+1)
    visited[start] = True
    cnt = 1
    while q:
        tower = q.popleft()
        for ntower in matrix[tower]:
            if not visited[ntower]:
                q.append(ntower)
                visited[ntower] = True
                cnt += 1
    return cnt
        
    
def solution(n, wires):
    matrix = [ [] for _ in range(n+1)]
    for u, v in wires:
        matrix[u].append(v)
        matrix[v].append(u)
    # 완전 탐색
    answer = 99999999
    for u, v in wires:
        del matrix[u][matrix[u].index(v)]
        del matrix[v][matrix[v].index(u)]
        answer = min(answer, abs(count_tower(matrix, u, n) - count_tower(matrix, v, n)))
        matrix[u].append(v)
        matrix[v].append(u)
    return answer
