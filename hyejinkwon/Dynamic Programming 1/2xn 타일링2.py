import sys

input = sys.stdin.readline
n = int(input())

# n = 1 -> 1가지
# n = 2 -> 3가지
# n = 3 -> 5가지
# n = 4 -> 11가지

dp = [0]*(n)

if n == 1 : 
    dp[n-1] = 1 
    print(dp[n-1]%10007)
elif n == 2 : 
    dp[n-1] = 3
    print(dp[n-1]%10007)
else :
    dp[0] = 1 
    dp[1] = 3

    for i in range(2,n) :
        dp[i] = dp[i-1] + dp[i-2]*2

    print(dp[n-1]%10007)