#1:15~25
import sys
s,k=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))

# 그냥 k+1개만큼 긴 길이 더하면 되는거 아닌가..?

dp=[0]*(len(arr))

for i in range(len(arr)):
    a=arr[i]
    if a%2==0:
        dp[i]=max(dp[:i])+1
print(dp)

# 1 2 4 3 1 5 6 7
# k만큼 빼서 연결하기 -> 맨 오른쪽에 있는 수로 하면 되고
# 연결 안됨 -> 거길 빼는거 취소, 더 왼쪽으로 가서 연결되는데 찾기..?