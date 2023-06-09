# 가로 2 세로 1을 이용해 세로 2 가로 n인 바닥 채우기 !
# 가로 n을 채우는 게 관건 : 2와 1을 이용해 합이 n을 만들 수 있느냐 ?
# DP 이용 !

# n = 1 -> 1         : 1
# n = 2 -> 11 2      : 2
# n = 3 -> 111 21 12 : 3
# n = 4 -> 1111 22 121 112 211 : 5
# dp[i] = dp[i-1] +dp[i-2]

def solution(n):
    answer = 0
    dp = [0] * n
    
    if n == 1:
        return 1
    if n == 2 :
        return 2

    if n >= 3 :
        dp[0], dp[1] = 1,2
        
        for i in range(2,n) :
            dp[i] = (dp[i-1] + dp[i-2])%1000000007
    
        answer = dp[-1]
        
        return answer