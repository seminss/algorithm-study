import sys
input = sys.stdin.readline

N, K = map(int, input().split())
bag = [[0,0]] # 무게와 가치 2가지고려 -> 2차원 배열 
dp = [[0]* (K+1) for _ in range(N+1)] # 행 : 물품 수 
                                      # 열 : 무게

for _ in range(N) :
    W, V = map(int,input().split())
    bag.append([W,V])

for i in range(1,N+1) :
    for j in range(1,K+1) :
        W,V = bag[i]

        if j < W : # 무게가 넘지 않는다면 
            dp[i][j] += dp[i-1][j]
        else :
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W]+V )

print(dp[N][K])