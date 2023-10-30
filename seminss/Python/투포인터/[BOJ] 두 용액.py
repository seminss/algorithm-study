#11:36~
import sys
import math
n=int(sys.stdin.readline())
aqua=list(map(int,sys.stdin.readline().split()))
aqua.sort() #O(nlogn)

right=n-1
left=0
result=[math.inf, math.inf]

while right>left:
    if abs(sum(result))>abs(aqua[right]+aqua[left]):
        result=[aqua[left],aqua[right]]
    if aqua[right]+aqua[left]>0:
        right-=1
    else:
        left+=1
print(result[0],result[1])