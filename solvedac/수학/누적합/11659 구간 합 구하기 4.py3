#11659 구간 합 구하기 4
import sys
n,m=map(int,sys.stdin.readline().split())
num=list(map(int,sys.stdin.readline().split()))
sum=[0]*(n)
sum[0]=num[0]

for i in range(1,n):
    sum[i]=sum[i-1]+num[i]
for j in range(m):
    a,b=map(int,sys.stdin.readline().split())
    if a==1:
        print(sum[b-1])
    else:
        print(sum[b-1]-sum[a-2])