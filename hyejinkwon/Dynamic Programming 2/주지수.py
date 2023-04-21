import sys

input = sys.stdin.readline
N, M = map(int, input().split())
town = []
dp = [[0]*(M+1) for _ in range(N+1)]
answer = []

for _ in range(N) : # 행 만큼 입력받기
    town.append(list(map(int, input().split())))

for i in range(1,N+1) :
    for j in range(1,M+1) :
        dp[i][j] = town[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

K = int(input())
for _ in range(K) :
    x1,y1,x2,y2 = map(int, input().split())
    answer.append(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])

for a in answer :
    print(a)