import sys
n=int(sys.stdin.readline())
dp=[0]*(n+6) #n이 5이하로 들어왔을 때 고려
dp[3]=1
dp[5]=1
for i in range(6,n+1):
    if dp[i-3]!=0 and dp[i-5]!=0:
        dp[i]=min(dp[i-3], dp[i-5])+1
    elif dp[i-3]!=0:
        dp[i]=dp[i-3]+1
    elif dp[i-5]!=0:
        dp[i]=dp[i-5]+1
if dp[n]!=0: print(dp[n])
else: print(-1)