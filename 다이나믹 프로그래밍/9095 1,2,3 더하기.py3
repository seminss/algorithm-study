import sys
T=int(sys.stdin.readline())
dp=[0]*12

for i in range(T):
    dp[1]=1
    dp[2]=2
    dp[3]=4
    n=int(sys.stdin.readline())
    for j in range(4,n+1,1):
        dp[j]=dp[j-3]+dp[j-2]+dp[j-1]
    print(dp[n])