#1:40
import sys
T=int(sys.stdin.readline())

for i in range(T):
    n=int(sys.stdin.readline())
    dp=[list(map(int,sys.stdin.readline().split())) for _ in range(2)]
    
    for j in range(1,n):
        if j==1:
            dp[0][j]+=dp[1][j-1]
            dp[1][j]+=dp[0][j-1]
        else:
            dp[0][j]+=max(dp[1][j-2],dp[1][j-1])
            dp[1][j]+=max(dp[0][j-2],dp[0][j-1])
    print(max(dp[0][n-1],dp[1][n-1]))