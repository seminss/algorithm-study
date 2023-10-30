#1:00~1:20
import sys
s,k=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))

dp=[0]*(len(arr))

for i in range(len(arr)):
    a=arr[i]
    if a%2==0:
        odd=0
        j=1
        while odd!=k+1 and i+j<len(arr):
            if arr[i+j]%2==0:
                dp[i]+=1
            else:
                odd+=1
            j+=1
        dp[i]+=1
print(max(dp))

#pypy만 시간초과가 안나네요..
#이 풀이는 dp가 아닌 것 같아요