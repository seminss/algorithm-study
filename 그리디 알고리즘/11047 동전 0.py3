import sys

n,k=map(int,sys.stdin.readline().split())
money=[]
for i in range(n):
    money.append(int(sys.stdin.readline()))

money.sort(reverse=True)
cnt=0

#그리디
tmp=k
for e in money:
    cnt+=tmp//e
    tmp=tmp%e

#나눠 떨어지는 경우
for e in money:
    if k%e==0 and k//e<cnt:
        cnt=k//e

print(cnt)