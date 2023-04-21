def solution(n):
    answer = 0
    dp=[0]*(n+1)
    for i in range(n+1):
        if i==1 or i==2:
            dp[i]=1
        else:
            dp[i]=dp[i-1]+dp[i-2]
    answer=dp[n]%1234567
    return answer