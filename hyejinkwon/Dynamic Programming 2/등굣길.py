from collections import deque 

dx = [1,0] # 오른쪽
dy = [0,1] # 아래

def solution(m, n, puddles):
    answer = 0
    puddles = [[q,p] for p,q in puddles]
    mapp = [[1]*(m+1) for _ in range(n+1)]
    dp = [[0]*(m+1) for _ in range(n+1)]
    
    dp[1][1] = 1
    for x,y in puddles :
        mapp[x][y] = 0
    
    for i in range(1,n+1) :
        for j in range(1,m+1):
            if i == 1 and j == 1 : continue
            # 왼쪽에서 + 위쪽에서 +
            if mapp[i][j] :
                dp[i][j] = (dp[i-1][j] + dp[i][j-1])%1000000007
            else :
                dp[i][j] = 0
            
    answer = dp[n][m]
    
    return answer