import sys

n=int(sys.stdin.readline())
dp=[0]*(n+1)
dp[1]=-1
for i in range(2,n+1):
    if i>=5 and (i-5)%5==0 and dp[i-5]!=-1:
        dp[i]=dp[i-5]+1
    elif i>=5 and (i-5)%2==0 and dp[i-5]!=-1:
        dp[i]=dp[i-5]+1
    elif i>=2 and (i-2)%5==0 and dp[i-2]!=-1:
        dp[i]=dp[i-2]+1
    elif i>=2 and (i-2)%2==0 and dp[i-2]!=-1:
        dp[i]=dp[i-2]+1
    else:
        dp[i]=-1
print(dp[n])