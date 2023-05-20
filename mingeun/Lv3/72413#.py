''' 2023.5.17
13:43 ~ 14:35
'''
INF = 2000000000


def solution(n, s, a, b, fares):
    # n:지점 개수(3~200) s:출발 a:도착 b:도착 fares:간선 비용
    # 간선 정보 초기화
    matrix = [[INF] * (n+1) for _ in range(n+1)]
    for start, end, cost in fares:
        matrix[start][end] = cost
        matrix[end][start] = cost
    for r in range(1, n+1):
        matrix[r][r] = 0
    # 모든 점에서 모든 점까지의 최단거리 계산
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])
    # 1 ~ n 지점까지 같이 이동한 후 나머지는 따로 이동
    answer = INF * n
    for i in range(1, n+1):
        answer = min(matrix[s][i] + matrix[i][a] + matrix[i][b], answer)
    return answer
