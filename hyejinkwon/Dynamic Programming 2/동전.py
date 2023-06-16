import sys

input = sys.stdin.readline
T = int(input())
coin = []
M_list = []

for t in range(T) :
    N = int(input())
    coin = list(map(int, input().split()))
    M = int(input())

    dp = [0] * (M+1)
    dp[0] = 1

    for c in coin : # 경우의 수로 DP 사용
        for i in range(M+1) :
            if i >= c :
                dp[i] += dp[i-c] #그 전 경우의 수에 더한다
        
    print(dp[M])