import sys
n=int(sys.stdin.readline())

dp=['']*(n+1)
if n<2:
    print('SK')
else:
    dp[1]='SK'
    dp[2]='CY'

    for i in range(3,n+1):
        dp[i]=dp[i-2]
    print(dp[n])