#2:23~
import sys
import math

n,s=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))

right=0
left=0
sum_v=0
res=math.inf

while right<n:
    #right는 이동
    sum_v+=arr[right]
    #sum_v>=s되면 s보다 작아지지 않는 선에서 left이동
    while sum_v>=s:
        res=min(res,right-left)        
        sum_v-=arr[left]
        left+=1
    right+=1
    
if res==math.inf: print(0)
else: print(res+1)