import sys

input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)
dp[0] = 0

if n == 0 :
    print(0)
    exit()

dp[1] = 1
if n == 1 :
    print(1)
    exit()
# f(0) = 0
# f(1) = 1

for i in range(2, n+1) :
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])