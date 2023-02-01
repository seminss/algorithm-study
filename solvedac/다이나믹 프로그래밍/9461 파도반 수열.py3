import sys
T=int(sys.stdin.readline())

for w in range(T):
    N=int(sys.stdin.readline())
    dp=[0]*(N+1)
    if N>0:
        dp[1]=1
    if N>1:
        dp[2]=1
    if N>2:
        dp[3]=1
    if N>3:
        for i in range(4,N+1):
            dp[i]=dp[i-3]+dp[i-2]
    print(dp[N])