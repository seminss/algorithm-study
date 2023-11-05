#12:07 ~ 12:17
def solution(land):
    answer = 0
    dp=[[0]*4 for _ in range(len(land))]
    dp[0]=land[0]
    for i in range(1,len(land)):
        for j in range(4):
            dp[i][j]=max([dp[i-1][w]+land[i][j] for w in range(4) if w is not j])
    answer=max(dp[len(land)-1])
    return answer