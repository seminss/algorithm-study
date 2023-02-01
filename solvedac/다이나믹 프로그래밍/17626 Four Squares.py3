import sys
num=int(sys.stdin.readline())
dp=[0]*(num+1)
dp[1]=1

for i in range(2,num+1):
    j=1
    std=4 #4이하의 제곱수로 표현 가능
    while((j**2)<=i): #무조건 4이하로 가능하니까
        std=min(std,dp[i-(j**2)])
        j+=1
    dp[i]=std+1
print(dp[num])