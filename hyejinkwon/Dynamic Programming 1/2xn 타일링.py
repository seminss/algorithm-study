import sys

input = sys.stdin.readline
n = int(input())

# n = 1 -> 1가지
# n = 2 -> 2가지
# n = 3 -> 3가지
# n = 4 -> 5가지

dp = [0]*(n)

if n == 1 : 
    dp[n-1] = 1 
    print(dp[n-1]%10007)
elif n == 2 : 
    dp[n-1] = 2
    print(dp[n-1]%10007)
else :
    dp[0] = 1 
    dp[1] = 2

    for i in range(2,n) :
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[n-1]%10007)