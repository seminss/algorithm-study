import sys
case=int(sys.stdin.readline())

for _ in range(case):
    n,m=map(int,sys.stdin.readline().split())
    arr=list(map(int,sys.stdin.readline().split()))
    dp=[0]*(m)

    # 금광 생성(행열 뒤집어서)
    gold=[[0]*(m) for _ in range(n+2)]
    for i in range(n):
        for j in range(m):
            gold[1+i][j]=arr[i*n+j]
    print(gold)
    result=0
    
    for y in range(1,n+1):
        idx=y
        dp[0]=gold[y][0]
        # print(idx)
        for x in range(1,m):
            mx=max(gold[idx-1][x],gold[idx][x],gold[idx+1][x])
            dp[x]=dp[x-1]+mx
            if mx==gold[idx-1][x]:
                idx=idx-1
            elif mx==gold[idx+1][x]:
                idx=idx+1
            # print(idx)
        # print(dp)
        if result<dp[m-1]:
            result=dp[m-1]
    print(result)