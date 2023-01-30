import sys
T=int(sys.stdin.readline())

dp=[(0,0)]*42

dp[0]=(1,0)
dp[1]=(0,1)
for w in range(T):
    n=int(sys.stdin.readline())
    for i in range(2,n+1):
        dp[i]=tuple(sum(elem) for elem in zip(dp[i-1],dp[i-2]))
    print(dp[n][0],dp[n][1])