''' 2023.5.14 
21:15 ~ 21:36
'''
def solution(land):
    answer = 0
    n = len(land)
    # dp[a][b] = a행 b열까지 밟았을때의 최대값
    dp = [[0]*4 for _ in range(n)]
    # 0행 초기화
    for i in range(4):
        dp[0][i] = land[0][i]
    # 나머지 계산
    for i in range(1, n):
        for j in range(4):
            # i행에서 어디를 밟아야 최대가 될것인지 계산
            max_result = 0
            for k in range(4):
                # 직전에 밟았던 열은 밟지 않는다.
                if k != j:
                    max_result = max(max_result, dp[i-1][k] + land[i][j])
            dp[i][j] = max_result
    return max(dp[n-1])
