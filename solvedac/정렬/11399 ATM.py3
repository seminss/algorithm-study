import sys
N=int(sys.stdin.readline())

person=list(map(int,sys.stdin.readline().split()))

person.sort()
cnt=[0]*N
cnt[0]=person[0]
sum=cnt[0]

for i in range(1,N):
    cnt[i]=person[i]+cnt[i-1]
    sum+=cnt[i]

print(sum)