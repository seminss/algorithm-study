import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))

dp=[0]*(max(arr)+1)
dp[arr[0]]=arr[0]

for i in range(len(arr)):
    a=arr[i]
    dp[a]=max(dp[:a])+a

print(max(dp))

# dp[arr[i]]에는 arr[i]까지 연속된 숫자의 sum 중 가장 큰 값이 저장되어 있다.
# dp[arr[i]] 원소보다 작은 값 중, 가장 큰 sum을 저장하고 있는 dp를 가져와서 현재 값을 더해준다. 
# dp[arr[i]]에 넣어준다.