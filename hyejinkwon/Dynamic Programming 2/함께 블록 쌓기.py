import sys
input = sys.stdin.readline

# 한 학생당 최대 1개의 블록 사용 가능
# 높이가 H인 탑 만들 수 있는 경우의 수

N,M,H = map(int,input().split())
dp = [[0] *(H+1) for _ in range(N+1)]
dp[0][0] = 1 # 초기값 

for i in range(1, N+1) :
    dp[i] = dp[i-1].copy() # 전 줄 복사
    block = list(map(int,input().split()))
    for b in block :
        for j in range(b, H+1):
            # 전 줄과 합이 H가 될 수 있는 경우의 수
            dp[i][j] += dp[i-1][j-b]

print(dp[N][M]%10007)