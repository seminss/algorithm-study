#2579 계단 오르기
import sys

f=int(sys.stdin.readline())
floor=[]
dp=[0]*300

for i in range(f):
    floor.append(int(sys.stdin.readline()))

#마지막은 무조건 밟는다고 생각하기(중간이든 찐 끝이든)
if f>0:
    dp[0]=floor[0]
if f>1:
    dp[1]=floor[0]+floor[1]
if f>2:
    dp[2]=max(floor[0]+floor[2],floor[1]+floor[2])
if f>3:
    for j in range(3,len(floor)):
        if dp[j-2]==dp[j-1]:
            dp[j]=dp[j-2]+floor[j]
        else:
            dp[j]=max(dp[j-2]+floor[j],dp[j-3]+floor[j]+floor[j-1])
print(dp[f-1])

