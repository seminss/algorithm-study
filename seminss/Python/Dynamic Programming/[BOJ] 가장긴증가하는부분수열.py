import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
dp=[0]*(max(arr)+1)
for i in arr:
    dp[i]=max(dp[:i])+1
print(max(dp))